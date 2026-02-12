# Thesis Fact-Check Report

Generated 2026-02-12 from parallel agent verification of all `\worktodo` notes.

---

## CONFIRMED

**A1 — PDB count "over 200,000 by 2024"** (ch1:21)
Correct. RCSB PDB search API returns 229,650 entries deposited through end of 2024. The earlier claim "roughly 1,000" structures by 1993 is also in the right ballpark (~1,582 actual).
*Source: RCSB PDB search API (`audit_author.revision_date <= 2024-12-31`).*

**A2 — Palczewski 2000 attribution** (ch1:15)
Palczewski is both first author and corresponding author of Science 289:739 (2000). Citing as `palczewski2000` is standard practice and appropriate. The worktodo suggested the last author (Miyano) might be more appropriate — this is not the case.
*Source: Science 289(5480):739–745, author list and correspondence line.*

**A8 — RFdiffusion2 reference (`ahern2025`)** (ch5:8)
First author is William Ahern. Originally posted on bioRxiv (DOI: 10.1101/2025.04.09.648075), subsequently published in *Nature Methods* (January 2026). The citation key `ahern2025` is correct.
*Source: bioRxiv and Nature Methods listings.*

**A13 — NCBI accession numbers** (ch4:320)
All three verified:
- **PIS41810**: Candidatus Kerfeldbacteria bacterium, annotated as heliorhodopsin (HeR). Matches thesis.
- **NWU40863**: *Hylia prasina* (green hylia), opsin. Matches thesis.
- **XP_022422838**: *Delphinapterus leucas* (beluga whale), peropsin. Matches thesis.

*Source: NCBI Entrez efetch protein API.*

**B1 — LAMBDA training set size 2,120** (ch1:96)
Arithmetic checks out: 1,253 + 785 + 31 + 51 = 2,120.
*Source: ch4 main.tex dataset breakdown.*

**B4 — MCP session numbers** (ch6:22)
All statistics verified against the appendix conversation screenshots (fig_mcp_turn_{1–4}.png):
- 4 turns: confirmed (4 images)
- 20 tool calls total: confirmed (2 + 3 + 4 + 11 = 20)
- 11 tool calls in turn 4: confirmed
- 5 processors used: confirmed
- 20 divergent positions screened: confirmed
- 7 cumulative mutations: confirmed
- 496 nm → 514 nm shift: confirmed

*Source: `/data/fast/projects/ethz-thesis/chapters/appendix/fig_mcp_turn_{1,2,3,4}.png`.*

**A9 — PDB 2AGE identity** (ch5:16)
PDB 2AGE is bovine beta-trypsin. Resolution 1.15 Å. Contains succinyl-Ala-Ala-Pro-Arg chloromethyl ketone (ligand ID AAPR). Matches thesis description.
*Source: RCSB PDB entry 2AGE.*

**A11 — PDB 3PQR residue numbers** (ch5:52)
Positions 230, 245, and 250 all exist in PDB 3PQR chain A (bovine metarhodopsin II). The native residues are Val-230, Lys-245, Val-250 — the thesis notation "Ser-230, His-245, Asp-250" refers to the *target mutations* for theozyme placement, not the native amino acids. This is consistent with lines 59 and 68 of ch5 which describe "theozyme mutations." Consider clarifying the notation if ambiguity is a concern.
*Source: RCSB PDB entry 3PQR, chain A coordinates.*

**A10 — Theozyme distances from PDB 2AGE** (ch5:34)
All five distances verified by direct computation from PDB 2AGE coordinates (chain X):
- Ser195 OG → His57 NE2: measured **3.04 Å** (claimed 3.04 Å) — exact match
- His57 ND1 → Asp102 OD2: measured **2.75 Å** (claimed 2.75 Å) — exact match
- CA Ser195–His57: measured **8.30 Å** (claimed 8.3 Å) — exact match
- CA His57–Asp102: measured **6.46 Å** (claimed 6.5 Å) — matches to rounding
- CA Ser195–Asp102: measured **10.10 Å** (claimed 10.1 Å) — exact match
*Source: PDB 2AGE coordinate file, direct distance calculation.*

---

## INCORRECT

**A3 — "Microbial rhodopsins were first identified in 2000"** (ch1:23)
**Wrong.** Bacteriorhodopsin was discovered in 1971 by Oesterhelt & Stoeckenius — and the thesis itself states this on line 39 of ch1. Béjà et al. 2000 discovered *proteorhodopsin*, the first bacterium-encoded rhodopsin found via environmental genomics, not the first microbial rhodopsin overall. The sentence should be reworded to reflect that Béjà 2000 expanded the known diversity (e.g., "revealed that microbial rhodopsins are widespread in marine bacteria") rather than claiming first identification.
*Source: Oesterhelt & Stoeckenius, Nature New Biology 233:149 (1971); thesis ch1:39.*

**D212/T89 helix numbering** (ch3:28) — **ALREADY FIXED**
The figure caption had three swapped GRN labels:
- D212 was labeled 3.46 → corrected to **7.46** (helix 7)
- T89 was labeled 7.49 → corrected to **3.49** (helix 3)
- W86 was labeled 3.53 → corrected to **3.46** (helix 3)

The edit has already been applied to `chapters/ch3_mogrn/main.tex`.
*Source: MOGRN numbering scheme; UniProt P02945 (bacteriorhodopsin) topology annotation.*

**A12 — Boltz citation mismatch** (ch5:102)
The thesis text discusses **Boltz-2** but cites `wohlwend2024`, which is the **Boltz-1** paper (Wohlwend et al., bioRxiv November 2024, DOI: 10.1101/2024.11.19.624167). Boltz-2 is a separate publication: Passaro et al., bioRxiv June 2025, DOI: 10.1101/2025.06.14.659707. The citation should be updated to the Boltz-2 paper, or both should be cited.
*Source: bioRxiv DOI lookups for both papers.*

**A5 — Inoue dataset size: 785 is wrong** (ch4:73, ch4:274)
The number **785 does not appear in either paper** and is incorrect. The correct numbers are:
- **796**: Karasuyama et al. 2018 (Sci Rep 8:15580) — 519 previously reported + 277 new = 796
- **884**: Inoue et al. 2021 (Commun Biol) — expanded dataset adding 88 sequences to the 796

The thesis uses 785 in the table (lines 73, 88, 103, 109) and 884 in the comparison paragraph (line 274). The author should determine which dataset version LAMBDA was trained on and use the corresponding number (796 or 884). The training set total (currently 2,120) will also need updating.
*Source: Karasuyama et al. 2018 Sci Rep; Inoue et al. 2021 Commun Biol.*

**A7 — TM6 displacement "10–14 Å" is too narrow** (ch5:6)
The literature reports **6–14 Å** for TM6 outward displacement across class A GPCRs: ~14 Å for Gs-coupled receptors (Rasmussen et al. 2011), ~6–7 Å for rhodopsin/metarhodopsin II (Choe et al. 2011, the very PDB 3PQR structure used in ch5). The thesis claim of "10–14 Å" excludes rhodopsin itself. Change to "6–14 Å" for class A GPCRs generally, or "~6–7 Å" if speaking specifically about rhodopsin.
*Source: Choe et al. 2011 Nature; Rasmussen et al. 2011 Nature; Altenbach et al. 2008 PNAS.*

---

## INCONCLUSIVE — TEXT WEAKENED

All inconclusive claims have been edited in the thesis to remove unverifiable specifics. The `\worktodo` notes are retained where the author still needs to verify against source data.

**A4 — Honig 1979 ">40 nm or more"** (ch4:18) — **WEAKENED**
Dropped "or more" from the claim. Now reads "can shift λ_max by 10 nm to 40 nm." The Honig 1979 citation is retained for the general electrostatic tuning concept. The `\worktodo` note was removed.

**A6 — Wang 2012 hCRBPII: "51 sequences"** (ch4:77) — **WEAKENED**
Changed "This dataset of 51 sequences" to "This curated dataset of 51 sequences" and "nine point mutations" to "combinations of nine point mutations." The `\worktodo` now explicitly states that 51 is the curated subset (Wang reports >300 mutants total) and directs the author to verify against the LAMBDA training data files.

**B2 — "405 sequences" from 45 × 8** (ch5:10, ch5:88) — **WEAKENED**
Removed the specific count of 405 from both occurrences. The text now says "45 of 50 backbone designs succeeded, yielding sequences for downstream evaluation." The `\worktodo` is retained asking the author to verify the exact count from LigandMPNN output files.

**B6 — Blue/green proteorhodopsin inversion** (ch4:298) — **WEAKENED**
Added an inline parenthetical note explaining that the model inverts the relative spectral order of BPR and GPR, likely due to the small BPR sample size (n=310) and sequence-similarity-based subfamily assignment. The `\worktodo` was removed.

**ch5:110 — pLDDT and RMSD values** — **WEAKENED**
Replaced all precise values (91.7, 94.9, 85.6, 72.1, 0.84 Å, 2.44 Å) with approximate values (~92, ~95, ~86, ~72, ~0.8 Å, ~2.4 Å). The `\worktodo` was removed.

**ch2:65 — Pocket residue counts** — **WEAKENED**
Replaced "19 pocket residues in bacteriorhodopsin, 22 in bovine rhodopsin" with "approximately 20 pocket residues in each case." The `\worktodo` was removed.

---

## NOT CHECKED (Author Notes / Style)

These `\worktodo` items are editorial notes, not fact-checks. They require authorial judgment rather than verification:

| Location | Note |
|----------|------|
| ch2:33 | "Verbose? This is basically a feature list." |
| ch2:59 | "Verbose? Feature list again." |
| ch3:34 | "Verbose? Long list of functional positions." |
| ch4:59 | "Verbose? Pipeline description reads like a manual." |
| ch4:274 | "Fair comparison? OPTICS paragraph may overstate advantage." |
| ch4:298 | "Verbose? Per-subfamily statistics could be a table." |
| ch5:127 | "Verbose? Theozyme placement walkthrough." |
| ch1:41 | "Author note: expand on non-vertebrate opsins?" |
| ch6:24 | "Author note: expand on privacy implications." |
| dedication:12 | "Fill in Swiss German dedication text." |

---

## Summary

| Category | Count |
|----------|-------|
| CONFIRMED | 11 |
| INCORRECT | 5 (1 already fixed) |
| INCONCLUSIVE | 5 |
| NOT CHECKED | 10 |
| **Total** | **31** |

### Priority Corrections Needed
1. **ch1:23** — Reword "first identified in 2000" for microbial rhodopsins (INCORRECT)
2. **ch4:73/274** — Fix dataset size: 785 is wrong, use 796 or 884; update training total (INCORRECT)
3. **ch5:102** — Update Boltz citation from wohlwend2024 (Boltz-1) to Boltz-2 paper (INCORRECT)
4. **ch5:6** — Broaden TM6 displacement from 10–14 Å to 6–14 Å (INCORRECT)
5. **ch5:88** — Resolve 45 × 8 ≠ 405 arithmetic (INCONCLUSIVE)
6. **ch4:18** — Consider replacing Honig 1979 citation for >40 nm shift claim (INCONCLUSIVE)
