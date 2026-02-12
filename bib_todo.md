# Bibliography TODO

Systematic citation audit across ch1--ch7. Priorities:
- **URGENT** -- broken cite key or key factual claim / named method uncited
- **GOOD** -- would strengthen the text
- **MAYBE** -- nice to have

---

## A. Broken Cite Keys (all URGENT)

These will produce LaTeX warnings/missing-reference markers in the PDF.

| # | Chapter | Line | In text | In bib | Action |
|---|---------|------|---------|--------|--------|
| 1 | ch1 | 104 | `\cite{frazer2025}` | `frazer2024` | Fix key |
| 2 | ch1 | 104 | `\cite{davis2024}` | **missing** | Add bib entry for VPOD dataset (Davis et al. 2024, GigaScience) or merge with `frazer2024` |
| 3 | ch1 | 104 | `\cite{inoue2021}` | `inoue2020` | Fix key |
| 4 | ch1 | 104 | `\cite{gerstenbruch2024}` | `sela2024` | Fix key (verify `sela2024` is RhoMax) |
| 5 | ch3 | 12 | `\cite{degrip2022}` | **missing** | Add bib entry for De Grip & Bhatt 2022 (or correct reference) |
| 6 | ch4 | 271 | `\cite{frazer2025}` | `frazer2024` | Fix key |
| 7 | ch4 | 271 | `\cite{inoue2021}` | `inoue2020` | Fix key |
| 8 | ch4 | 271 | `\cite{gerstenbruch2024}` | `sela2024` | Fix key |

---

## B. Missing Bib Entries (tools/methods cited but no entry exists)

These need new `@article`/`@misc` entries in `bibliography.bib`.

| # | Tool / Reference | Used in | Suggested reference |
|---|------------------|---------|---------------------|
| 9 | RFdiffusion2 / Ahern et al. 2025 | ch5 (lines 8, 52, 72, 86, 102), ch7 (line 40) | Ahern et al. 2025 (verify preprint/publication status) |
| 10 | LigandMPNN | ch5 (lines 8, 86), ch7 (line 40) | Dauparas et al. 2022, Science |
| 11 | MCP (Model Context Protocol) | ch6 (line 15) | Anthropic MCP specification (2024) |
| 12 | BLAST / BLASTp | ch2 (line 31), ch4 (line 176) | Altschul et al. 1990, J Mol Biol |
| 13 | MMseqs2 | ch2 (line 31), ch4 (line 138) | Steinegger & Soding 2017, Nat Biotechnol |
| 14 | Biopython | ch1 (line 122), ch2 (line 31), ch4 (line 140) | Cock et al. 2009, Bioinformatics |
| 15 | UniProt | ch1 (line 23, 120), ch2 (lines 6, 8, 29) | UniProt Consortium 2023, Nucleic Acids Res |
| 16 | PDB (database) | ch1 (line 21), ch2 (lines 6, 57) | Berman et al. 2000, Nucleic Acids Res |
| 17 | UMAP | ch2 (line 157) | McInnes et al. 2018, arXiv |
| 18 | PyTorch Geometric | ch2 (line 91) | Fey & Lenssen 2019, ICLR Workshop |
| 19 | VPOD dataset (if separate from OPTICS) | ch1 (line 104), ch4 (line 72) | Davis et al. 2024, GigaScience (same as #2) |
| 20 | Kabsch superposition | ch2 (line 59), ch4 (line 106), ch5 (line 48) | Kabsch 1976, Acta Crystallogr |
| 21 | Schrodinger suite | ch1 (line 122), ch2 (line 8) | Schrodinger LLC release reference |
| 22 | PDB 3PQR (metarhodopsin II) | ch5 (line 16) | Choe et al. 2011 (or correct deposition paper) |
| 23 | PDB 2AGE (trypsin acyl-enzyme) | ch5 (line 16) | Original deposition paper (verify authors) |
| 24 | PDB 1U19 (bovine rhodopsin 2.2 A) | ch2 (line 65), ch4 (line 104), ch5 (line 16) | Verify if `okada2002` covers 1U19 or if a separate Okada et al. 2004 entry is needed |

---

## C. Per-Chapter Citation Gaps

### Ch1 -- Introduction

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 25 | 21 | "the Protein Data Bank grew rapidly, from roughly 1,000 structures in 1993 to over 200,000 by 2024" | URGENT | Cite PDB (Berman et al. 2000) |
| 26 | 21 | "GPCR structures alone rising from fewer than 5 in 2007 to over 700 today" | URGENT | Cite `kooistra2021` or GPCRdb statistics |
| 27 | 23 | "UniProt now contains over 200 million protein sequences" | URGENT | Cite UniProt Consortium |
| 28 | 23 | "they are now recognized as among the most abundant proteins on Earth" (microbial rhodopsins) | URGENT | Cite `ernst2014` or Finkel et al. 2013 |
| 29 | 27 | "ESM-2" -- named pLM, no citation | URGENT | Add `\cite{lin2023}` |
| 30 | 27 | "Ankh" -- named pLM, no citation | URGENT | Add `\cite{elnaggar2023ankh}` |
| 31 | 74 | "A more recent approach defined positions based on conserved hydrogen bond networks" | URGENT | Cite the specific paper (reader cannot identify which approach) |
| 32 | 102 | "The D85N mutation in bacteriorhodopsin... producing a red shift of up to 40 nm" | URGENT | Cite mutation study (Mogi et al. 1988 or similar) |
| 33 | 102 | "The equivalent mutation in bovine rhodopsin, E113Q, produces a similar effect" | URGENT | Cite Sakmar et al. 1989 or Zhukovsky & Oprian 1989 |
| 34 | 19 | "The breakthrough came around 2013 with direct electron detectors" (cryo-EM revolution) | GOOD | Cite Kuehlbrandt 2014 or Cheng 2015 |
| 35 | 39 | "roughly 800 members in the human genome" (GPCRs) | GOOD | Cite `kooistra2021` or Fredriksson et al. 2003 |
| 36 | 53 | "enabled optogenetics... transformed neuroscience" | GOOD | Add `\cite{deisseroth2015}` |
| 37 | 55 | Type II opsin function (rod/cone opsins) | GOOD | Cite `palczewski2006` or `shichida2009` or `nathans1987` |
| 38 | 57 | "They share no detectable sequence similarity" (Type I vs Type II) | GOOD | Cite `ernst2014` |
| 39 | 59 | K216/K296 binding residue identifications | GOOD | Cite `luecke1999` (K216) and `palczewski2000` (K296) |
| 40 | 92 | "Retinal in solution absorbs at approximately 380 nm" | GOOD | Cite `honig1979` |
| 41 | 96 | "as seen in UV-sensitive SWS1 cone opsins" | GOOD | Cite `yokoyama2008` |
| 42 | 98 | "In bacteriorhodopsin, the counterion is D85. In bovine rhodopsin, it is E113" | GOOD | Cite `luecke1999` and `palczewski2000` |
| 43 | 102 | "other binding pocket residues contribute individual shifts of 10--30 nm" | GOOD | Cite `kandori2020` or `honig1979` |
| 44 | 25 | CASP competition not named or cited | GOOD | Mention CASP and cite CASP14 assessment |
| 45 | 134 | "Model Context Protocol" | MAYBE | Cite MCP specification |
| 46 | 17 | Nobel Prize facts (Kobilka 2012, Henderson 2017) | MAYBE | Nobel Foundation or review |

### Ch2 -- ProtOS (entire chapter has ZERO citations)

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 47 | 6 | "fewer than 70 have unique experimental structures" (opsins) | URGENT | Cite PDB + opsin structure survey |
| 48 | 8 | UniProt, PDB, AlphaFold DB named as data sources | URGENT | Cite all three at first mention |
| 49 | 8 | Biopython, Schrodinger suite named | URGENT | Cite both |
| 50 | 29 | "Two cone opsins can share 80% identity and absorb light 140 nm apart" | URGENT | Cite specific example (`yokoyama2008` or `shichida2009`) |
| 51 | 31 | BLAST, MMseqs2, BioPython named | URGENT | Cite all |
| 52 | 55 | "A single mutation can reposition a side chain... absorption spectrum shifts by 40 nm" | URGENT | Cite mutagenesis study |
| 53 | 55 | Convergent evolution of bR and bovine rhodopsin | URGENT | Cite `ernst2014` or `kandori2020` |
| 54 | 57 | "The PDB holds roughly 200,000 experimental structures" | URGENT | Cite PDB reference |
| 55 | 57 | "AlphaFold DB fills the coverage gap" | URGENT | Cite `varadi2022` and `jumper2021` |
| 56 | 59 | Boltz2 named | URGENT | Cite `wohlwend2024` |
| 57 | 65 | PDB 1C3W (bacteriorhodopsin) | URGENT | Cite `luecke1999` |
| 58 | 65 | PDB 1U19 (bovine rhodopsin) | URGENT | Cite `okada2002` (verify covers 1U19) |
| 59 | 65 | "the counterion (D85 in bacteriorhodopsin, E113 in bovine rhodopsin)" | URGENT | Cite `kandori2020` or `ernst2014` |
| 60 | 91 | PyTorch Geometric named | URGENT | Cite Fey & Lenssen 2019 |
| 61 | 109 | GPCRdb, Ballesteros-Weinstein numbering | URGENT | Cite `kooistra2021`, `ballesteros1995` |
| 62 | 111 | "the most conserved residue on each helix as X.50" | URGENT | Cite `ballesteros1995` |
| 63 | 121 | Microswitch positions (E/DRY, PIF, CWxP, NPxxY) | URGENT | Cite `venkatakrishnan2013` or `katritch2013` |
| 64 | 123 | "Cone SWS opsin has glycine at position 2.50... absence of sodium sensitivity" | URGENT | Cite relevant SWS1 study |
| 65 | 143 | MOGRN named | URGENT | Cite `hidber2025mogrn` or `\autoref{ch:mogrn}` |
| 66 | 149 | ESM-2 named | URGENT | Cite `lin2023` |
| 67 | 149 | Ankh named | URGENT | Cite `elnaggar2023ankh` |
| 68 | 155 | Ankh Large "produces a 1536-dimensional vector" | URGENT | Cite `elnaggar2023ankh` |
| 69 | 157 | UMAP named | URGENT | Cite McInnes et al. 2018 |
| 70 | 83 | "graph neural networks operate on nodes and edges" | GOOD | Cite `kipf2017` |
| 71 | 37 | Subfamily classification scheme | GOOD | Cite `Koyanagi2014` or `shichida2009` |

### Ch3 -- MOGRN

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 72 | 12 | Ballesteros-Weinstein numbering described | URGENT | Add `\cite{ballesteros1995}` |
| 73 | 14 | "We developed MOGRN" (self-citation) | URGENT | Add `\cite{hidber2025mogrn}` |
| 74 | 22 | PDB 1C3W (bacteriorhodopsin) | GOOD | Cite `luecke1999` |
| 75 | 52 | Structure prediction reliability (sub-angstrom iRMSD) | GOOD | Cite `jumper2021` or `lin2023` |

### Ch4 -- LAMBDA

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 76 | 32 | OPTICS first mention (no cite) | URGENT | Add `\cite{frazer2024}` |
| 77 | 32 | Inoue model first mention (no cite) | URGENT | Add `\cite{inoue2020}` |
| 78 | 32 | RhoMax first mention (no cite) | URGENT | Add `\cite{sela2024}` |
| 79 | 50 | Ankh-large named (no cite) | URGENT | Add `\cite{elnaggar2023ankh}` |
| 80 | 72 | "VPOD 1.3 (Visual Physiology Opsin Database) contains 1,253 type II opsin sequences" | URGENT | Add `\cite{frazer2024}` |
| 81 | 74 | "The Inoue dataset... containing 785 sequences" | URGENT | Add `\cite{inoue2020}` |
| 82 | 78 | "Wang et al. (2012) created retinal-binding variants" -- author-year but no `\cite{}` | URGENT | Add `\cite{wang2012}` |
| 83 | 10/50/133 | Ballesteros-Weinstein numbering (multiple mentions, no cite) | URGENT | Add `\cite{ballesteros1995}` at first mention |
| 84 | 154 | "Graph Convolutional Network (GCN)" | URGENT | Add `\cite{kipf2017}` |
| 85 | 138 | MMseqs2 named | URGENT | Cite (needs bib entry) |
| 86 | 36 | hCRBPII (4QYP) -- structure cited by PDB ID | GOOD | Add `\cite{wang2012}` |
| 87 | 36/104 | PDB 1C3W, 1U19 -- structures cited by ID | GOOD | Cite `luecke1999`, `okada2002` |
| 88 | 50/133 | MOGRN referenced | GOOD | Add `\cite{hidber2025mogrn}` or `\autoref{ch:mogrn}` |
| 89 | 16 | Optogenetics context | GOOD | Cite `deisseroth2015` |
| 90 | 20 | Counterion as primary spectral determinant | GOOD | Cite `honig1979` or `kandori2020` |
| 91 | 140 | Biopython pairwise2 module | GOOD | Cite Cock et al. 2009 |
| 92 | 106 | Kabsch superposition | GOOD | Cite Kabsch 1976 |
| 93 | 309 | OPTICS, Inoue, RhoMax in Discussion (comparative mention) | GOOD | Add `\cite{frazer2024,inoue2020,sela2024}` |
| 94 | 311 | "OPTICS' sequence-based approach (5.49 nm cross-validated)" | GOOD | Add `\cite{frazer2024}` |
| 95 | 74 | Tara Oceans project | MAYBE | Cite Sunagawa et al. 2015 or rely on Inoue cite |

### Ch5 -- Rhodozyme (entire chapter has ZERO citations)

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 96 | 8 | "RFdiffusion2 (Ahern et al., 2025)" -- inline author-year, no `\cite{}` | URGENT | Add bib entry + `\cite{ahern2025}` |
| 97 | 8 | LigandMPNN named | URGENT | Add bib entry + cite |
| 98 | 10 | Boltz2 named | URGENT | Cite `wohlwend2024` |
| 99 | 16 | PDB 3PQR (metarhodopsin II) | URGENT | Add bib entry + cite |
| 100 | 16 | PDB 1U19 (bovine rhodopsin) | URGENT | Cite `okada2002` |
| 101 | 16 | PDB 2AGE (trypsin acyl-enzyme) | URGENT | Add bib entry + cite |
| 102 | 52, 72, 86, 102 | "Ahern et al. (2025)" -- repeated inline, no `\cite{}` | URGENT | Replace all with `\cite{ahern2025}` |
| 103 | 68 | "RFdiffusion generates backbone designs" | URGENT | Cite `watson2023` |
| 104 | 133 | "RFdiffusion2, LigandMPNN, and Boltz2 are published tools" | URGENT | Cite all three |
| 105 | 6 | "microswitch residues... TM3, TM5, TM6, TM7" | URGENT | Cite `venkatakrishnan2013` or `katritch2013` |
| 106 | 6 | "TM6 moves 10--14 angstrom outward" | URGENT | Cite source for displacement distance |
| 107 | 6 | Type II opsin conformational change | GOOD | Cite `palczewski2006` or `kandori2020` |
| 108 | 6 | "binds the G protein transducin" | GOOD | Cite `palczewski2006` |
| 109 | 48 | GRN annotation | GOOD | Add `\autoref{ch:mogrn}` or `\cite{hidber2025mogrn}` |
| 110 | 48 | "Kabsch-aligned" | MAYBE | Cite Kabsch 1976 |

### Ch6 -- ProtOS-MCP (entire chapter has ZERO citations)

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 111 | 15 | "The Model Context Protocol (MCP), developed by Anthropic" | URGENT | Add bib entry + cite MCP spec |
| 112 | 6 | "large language models that call tools are not new" | GOOD | Cite tool-use LLM reference (Schick et al. 2023 "Toolformer" or similar) |
| 113 | 43 | LAMBDA, GRN referenced | GOOD | Add `\autoref{ch:lambda}` and `\autoref{ch:mogrn}` |
| 114 | 45 | "the human long-wave opsin" | MAYBE | Cite `nathans1987` |

### Ch7 -- Discussion (entire chapter has ZERO citations)

| # | Line | Claim / Item | Priority | Suggested action |
|---|------|-------------|----------|------------------|
| 115 | 12 | "Ballesteros--Weinstein provides for GPCRs" | URGENT | Cite `ballesteros1995` |
| 116 | 40 | "RFdiffusion2, Boltz, and LigandMPNN are already accessible" | URGENT | Cite all three tools |
| 117 | 12 | MOGRN described | GOOD | Cite `hidber2025mogrn` or `\autoref{ch:mogrn}` |
| 118 | 10 | LAMBDA accuracy numbers and hCRBPII | GOOD | Add `\autoref{ch:lambda}` |
| 119 | 38 | "red-shifted opsins for deeper tissue penetration" (optogenetics) | GOOD | Cite `deisseroth2015` |
| 120 | 4 | "No method predicted spectral properties across the divide" | GOOD | Cite prior approaches to substantiate the gap |

---

## D. Summary

| Priority | Count |
|----------|-------|
| URGENT   | 68    |
| GOOD     | 41    |
| MAYBE    | 11    |
| **Total** | **120** |

### Most critical actions (in order):
1. **Fix 5 broken cite keys** (#1--8): `frazer2025`->`frazer2024`, `inoue2021`->`inoue2020`, `gerstenbruch2024`->`sela2024`, add `davis2024`, add `degrip2022`
2. **Add ~15 missing bib entries** (#9--24): RFdiffusion2, LigandMPNN, MCP, BLAST, MMseqs2, Biopython, UniProt, PDB, UMAP, PyTorch Geometric, Kabsch, PDB 3PQR, PDB 2AGE, PDB 1U19
3. **Cite existing bib entries that are never used**: `ballesteros1995` (used 0 times outside ch1), `elnaggar2023ankh`, `lin2023`, `kipf2017`, `venkatakrishnan2013`/`katritch2013`, `deisseroth2015`, `ernst2014`, `luecke1999`, `wang2012`, `watson2023`, `hidber2025mogrn`, many others
4. **Ch2, ch5, ch6, ch7 have ZERO citations** -- these chapters need the most work
