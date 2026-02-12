#!/usr/bin/env python3
"""
fix_bib.py — Verify and fix BibTeX entries using CrossRef DOI lookups.

Usage:
    python3 fix_bib.py bibliography.bib
    python3 fix_bib.py bibliography.bib -o fixed_bibliography.bib
    python3 fix_bib.py bibliography.bib --dry-run   # just report issues, don't fix

Requires: pip install requests
"""

import re
import sys
import json
import time
import argparse
import requests
from pathlib import Path
from difflib import unified_diff

# ─── Minimal BibTeX parser ───────────────────────────────────────────────────

def parse_bib(text: str) -> list[dict]:
    """Parse a .bib file into a list of entry dicts, preserving raw text."""
    entries = []
    # Match each @type{key, ... } block
    pattern = re.compile(
        r'(@\w+\s*\{[^@]*?\n\})', re.DOTALL
    )
    for match in pattern.finditer(text):
        raw = match.group(1)
        entry = {'_raw': raw, '_start': match.start(), '_end': match.end()}

        # Entry type and key
        header = re.match(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', raw)
        if not header:
            continue
        entry['_type'] = header.group(1).lower()
        entry['_key'] = header.group(2)

        # Parse fields
        for field_match in re.finditer(
            r'(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}', raw
        ):
            field_name = field_match.group(1).lower()
            field_value = field_match.group(2).strip()
            entry[field_name] = field_value

        entries.append(entry)
    return entries


def clean_latex(text: str) -> str:
    """Remove LaTeX markup for comparison purposes."""
    text = re.sub(r'\{\\["\'^`~cv]\s*\{?(\w)\}?\}?', r'\1', text)
    text = re.sub(r'\\["\'^`~cv]\s*\{?(\w)\}?', r'\1', text)
    text = re.sub(r'[{}\\$]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ─── CrossRef lookup ─────────────────────────────────────────────────────────

CROSSREF_API = "https://api.crossref.org/works/"
HEADERS = {
    "User-Agent": "BibFixer/1.0 (mailto:your@email.com)",
    "Accept": "application/json",
}


def fetch_crossref(doi: str) -> dict | None:
    """Fetch metadata from CrossRef for a given DOI."""
    url = CROSSREF_API + requests.utils.quote(doi, safe='')
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 200:
            return resp.json().get("message", {})
        elif resp.status_code == 404:
            return None
        else:
            print(f"  ⚠ CrossRef returned {resp.status_code} for {doi}")
            return None
    except requests.RequestException as e:
        print(f"  ⚠ Request failed for {doi}: {e}")
        return None


def crossref_authors(cr: dict) -> str | None:
    """Convert CrossRef author list to BibTeX format."""
    authors = cr.get("author", [])
    if not authors:
        return None
    parts = []
    for a in authors:
        family = a.get("family", "")
        given = a.get("given", "")
        if family and given:
            parts.append(f"{family}, {given}")
        elif family:
            parts.append(family)
    return " and ".join(parts) if parts else None


def crossref_pages(cr: dict) -> str | None:
    """Extract pages from CrossRef metadata."""
    pages = cr.get("page")
    if pages:
        return pages.replace("-", "--") if "-" in pages and "--" not in pages else pages
    return None


def crossref_title(cr: dict) -> str | None:
    """Extract title from CrossRef."""
    titles = cr.get("title", [])
    return titles[0] if titles else None


def crossref_journal(cr: dict) -> str | None:
    """Extract journal name from CrossRef."""
    names = cr.get("container-title", [])
    return names[0] if names else None


def crossref_year(cr: dict) -> str | None:
    """Extract publication year from CrossRef."""
    issued = cr.get("issued", {})
    parts = issued.get("date-parts", [[]])
    if parts and parts[0] and parts[0][0]:
        return str(parts[0][0])
    return None


def crossref_volume(cr: dict) -> str | None:
    return cr.get("volume")


def crossref_number(cr: dict) -> str | None:
    return cr.get("issue")


# ─── Comparison and fixing ───────────────────────────────────────────────────

def normalize(text: str) -> str:
    """Normalize text for comparison: lowercase, strip punctuation, collapse spaces."""
    text = clean_latex(text)
    text = re.sub(r'[^\w\s]', '', text.lower())
    return re.sub(r'\s+', ' ', text).strip()


def fields_match(local: str | None, remote: str | None) -> bool:
    """Check if two field values are effectively the same."""
    if local is None or remote is None:
        return True  # Can't compare if one is missing
    return normalize(local) == normalize(remote)


def compare_entry(entry: dict, cr: dict) -> list[dict]:
    """Compare a bib entry with CrossRef data, return list of discrepancies."""
    issues = []

    checks = [
        ("title",   entry.get("title"),   crossref_title(cr)),
        ("journal", entry.get("journal"), crossref_journal(cr)),
        ("year",    entry.get("year"),    crossref_year(cr)),
        ("volume",  entry.get("volume"),  crossref_volume(cr)),
        ("number",  entry.get("number"),  crossref_number(cr)),
        ("pages",   entry.get("pages"),   crossref_pages(cr)),
    ]

    for field, local, remote in checks:
        if remote is None:
            continue
        if not fields_match(local, remote):
            issues.append({
                "field": field,
                "local": local,
                "remote": remote,
            })

    # Author check (more lenient — just check last names)
    local_authors = entry.get("author", "")
    remote_authors = crossref_authors(cr)
    if local_authors and remote_authors:
        local_lastnames = set(
            normalize(p.split(",")[0]) for p in local_authors.split(" and ")
        )
        remote_lastnames = set(
            normalize(p.split(",")[0]) for p in remote_authors.split(" and ")
        )
        if local_lastnames != remote_lastnames:
            missing = remote_lastnames - local_lastnames
            extra = local_lastnames - remote_lastnames
            if missing or extra:
                issues.append({
                    "field": "author",
                    "local": f"({len(local_lastnames)} authors)",
                    "remote": f"({len(remote_lastnames)} authors)",
                    "detail": {
                        "missing_from_local": sorted(missing) if missing else [],
                        "extra_in_local": sorted(extra) if extra else [],
                    }
                })

    return issues


def apply_fix(raw: str, field: str, old_val: str | None, new_val: str) -> str:
    """Replace a field value in the raw BibTeX entry string."""
    if old_val is None:
        # Field doesn't exist — insert before closing }
        insertion = f"  {field:<10}= {{{new_val}}},\n"
        raw = raw.rstrip().rstrip('}') + insertion + '}'
        return raw

    # Escape for regex
    escaped = re.escape(old_val)
    pattern = re.compile(
        rf'({field}\s*=\s*\{{)' + escaped + r'(\})',
        re.IGNORECASE
    )
    result = pattern.sub(rf'\g<1>{new_val}\2', raw)
    if result == raw:
        # Fallback: simple string replace
        result = raw.replace(old_val, new_val, 1)
    return result


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fix BibTeX entries using CrossRef")
    parser.add_argument("bibfile", help="Path to .bib file")
    parser.add_argument("-o", "--output", help="Output file (default: overwrites input)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report issues without modifying the file")
    parser.add_argument("--skip-authors", action="store_true",
                        help="Don't auto-fix author fields (they often have LaTeX)")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between CrossRef requests in seconds (default: 0.3)")
    args = parser.parse_args()

    bib_path = Path(args.bibfile)
    text = bib_path.read_text(encoding="utf-8")
    entries = parse_bib(text)

    doi_entries = [(e, e["doi"]) for e in entries if "doi" in e]
    print(f"Found {len(entries)} entries, {len(doi_entries)} with DOIs.\n")

    total_issues = 0
    fixes_applied = 0
    modified_text = text

    for i, (entry, doi) in enumerate(doi_entries):
        key = entry['_key']
        print(f"[{i+1}/{len(doi_entries)}] {key} (DOI: {doi})")

        cr = fetch_crossref(doi)
        if cr is None:
            print(f"  ✗ DOI not found on CrossRef\n")
            continue

        issues = compare_entry(entry, cr)
        if not issues:
            print(f"  ✓ OK\n")
            continue

        total_issues += len(issues)
        for issue in issues:
            field = issue["field"]
            local = issue["local"]
            remote = issue["remote"]

            if "detail" in issue:
                detail = issue["detail"]
                missing = detail.get("missing_from_local", [])
                extra = detail.get("extra_in_local", [])
                print(f"  ⚠ {field}: {local} → {remote}")
                if missing:
                    print(f"       Missing: {', '.join(missing)}")
                if extra:
                    print(f"       Extra:   {', '.join(extra)}")
                # Don't auto-fix authors by default (LaTeX accents are tricky)
                if args.skip_authors or field == "author":
                    print(f"       (skipped — use manual review for authors)")
                    continue
            else:
                print(f"  ⚠ {field}:")
                print(f"       local:  {local}")
                print(f"       crossref: {remote}")

            if not args.dry_run and field != "author":
                old_raw = entry['_raw']
                new_raw = apply_fix(old_raw, field, local, remote)
                if new_raw != old_raw:
                    modified_text = modified_text.replace(old_raw, new_raw)
                    entry['_raw'] = new_raw  # update for subsequent fixes
                    fixes_applied += 1
                    print(f"       → FIXED")

        print()
        time.sleep(args.delay)

    # Summary
    print("=" * 60)
    print(f"Entries checked:  {len(doi_entries)}")
    print(f"Issues found:     {total_issues}")
    if not args.dry_run:
        print(f"Fixes applied:    {fixes_applied}")

    # Write output
    if not args.dry_run and fixes_applied > 0:
        out_path = Path(args.output) if args.output else bib_path
        out_path.write_text(modified_text, encoding="utf-8")
        print(f"Written to: {out_path}")
    elif args.dry_run:
        print("\n(Dry run — no changes written)")
    else:
        print("\nNo fixes needed!")


if __name__ == "__main__":
    main()
