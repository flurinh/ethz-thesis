# Figure Index

Maps source image files (from `figures_12_2.zip`) to thesis figures.

## Chapter 1 — Introduction

| Source file | Dimensions | Thesis figure | Label | Description |
|-------------|-----------|---------------|-------|-------------|
| `1_1.jpg` | 1023x1021 | Figure 1.1 | `fig:type1-type2-comparison` | Structural comparison of Type I and Type II opsins (A,B: full structures; C,D: binding pocket close-ups) |
| `1_2.jpg` | 607x349 | Figure 1.2 | `fig:charge-distribution` | Charge distribution along the retinal chromophore (blue-to-red gradient) |

## Chapter 2 — ProtOS

| Source file | Dimensions | Thesis figure | Label | Description |
|-------------|-----------|---------------|-------|-------------|
| `2_1.jpg` | 1260x1104 | Figure 2.1 | `fig:protos-overview` | ProtOS architecture overview (A: ProtosPath/Entity/Registry; B: Processors; C: Model Manager) |
| `2_3.jpg` | 1134x640 | Code snippet | — | Sequence Processor code example |
| `2_4.jpg` | 1177x1036 | Figure 2.2 | `fig:opsin-diversity` | Per-subfamily sequence identity distributions (ridge plot, 9 subfamilies) |
| `2_5.jpg` | 1134x637 | Code snippet | — | Structure Processor code example |
| `2_6.jpg` | 1546x709 | Figure 2.3 | `fig:br-bovine-aligned` | Retinal-aligned overlay of bacteriorhodopsin and bovine rhodopsin (A: bR blue; B: bovine pink; C: overlay) |
| `2_7.jpg` | 1129x586 | Code snippet | — | Graph Processor code example |
| `2_8.jpg` | 702x1174 | Figure 2.4 | `fig:pocket-graphs` | Binding pocket graph for bovine rhodopsin (A: structure with pocket residues; B: contact graph colored by TM helix) |
| `2_9.jpg` | 1134x499 | Code snippet | — | GRN Processor code example |
| `2_10.jpg` | 1636x879 | Figure 2.5a | `fig:grn-alignment` | GRN microswitch and spectral tuning table (9 opsins x 18 GRN positions, color-coded). **Landscape layout.** |
| `2_11.jpg` | 1035x792 | Figure 2.5b | `fig:grn-microswitches` | GRN positions mapped onto bovine rhodopsin (two views with labeled positions) |
| `2_12.jpg` | 1135x501 | Code snippet | — | Embedding Processor code example |
| `2_13.jpg` | 1153x865 | Figure 2.6 | `fig:atlas-umap` | UMAP projection of Ankh Large embeddings (27,639 opsins, 13 subfamilies) |
| `2_14.jpg` | 1129x541 | Code snippet | — | Property Processor code example |
| `2_15.jpg` | 1129x498 | Code snippet | — | Model Manager code example |

## Chapter 3 — MOGRN

| Source file | Dimensions | Thesis figure | Label | Description |
|-------------|-----------|---------------|-------|-------------|
| `3_1.jpg` | 778x1081 | Figure 3.1 | `fig:mogrn-1c3w` | Key MOGRN positions on bacteriorhodopsin (K216=7.50, D85=3.45, D212=7.46, retinal in rust). Portrait layout. |

## Chapter 4 — LAMBDA

| Source file | Dimensions | Thesis figure | Label | Description |
|-------------|-----------|---------------|-------|-------------|
| `4_1.jpg` | 2287x714 | Figure 4.1 | `fig:spectral-tuning-overview` | Spectral tuning overview (A: E=hc/lambda curve; B: retinal Schiff base configurations; C: 11-cis histogram; D: all-trans histogram). **Landscape layout.** |
| `4_2.jpg` | 1351x1036 | Figure 4.2 | `fig:pocket-structures-graphs` | Binding pocket structures and graphs for three protein families (A-C: structures; D-F: contact graphs for bR, bovine rhodopsin, hCRBPII) |
| `4_3a.jpg` | 2163x816 | Figure 4.3 | `fig:data-flow` | Data flow for binding pocket graph construction (sequence and structure pathways) |
| `4_3b.png` | 2206x1300 | Figure 4.4 | `fig:lambda-model` | LAMBDA model architecture (Encoder → Pooling → Multi-Task Prediction Heads → Inference Logic) |
| `4_4.jpg` | 2275x781 | Figure 4.5 | `fig:lambda-distributions` | Training data distributions (A: 11-cis lambda_max; B: all-trans lambda_max by dataset source) |
| `4_5.jpg` | 2.6 | `fig:lambda-results` | Predicted vs measured lambda_max scatter (A: Type I all-trans; B: Type II 11-cis, with ±5/±10 nm bands) |
| `4_6.jpg` | 1990x1128 | Figure 4.7 | `fig:opsin-atlas` | Opsin Atlas spectral landscape (A: 20,061 Type I; B: 27,639 Type II; C: spectral separation). **Landscape layout.** |

## Chapter 5 — Rhodozyme

| Source file | Dimensions | Thesis figure | Label | Description |
|-------------|-----------|---------------|-------|-------------|
| `5_1.jpg` | 1063x715 | Figure 5.1 | `fig:rhodozyme-input` | Input structures (A: dark/active rhodopsin overlay with TM5/6 displacement; B: trypsin catalytic triad with substrate) |
| `5_2.jpg` | 1132x823 | Figure 5.2 | `fig:theozyme-extraction` | Theozyme extraction (Ser-His-Asp triangle with Ca distances: 8.3/6.5/10.1 A and Cb direction vectors) |
| `5_3.jpg` | 1200x831 | Figure 5.3 | `fig:theozyme-placement` | Theozyme placement on rhodopsin scaffold (A: full structure from ICL face; B: alternate angle) |
| `5_4.jpg` | 463x774 | Figure 5.4 | `fig:rfdiffusion-mask` | RFdiffusion mask (gray: locked TM core; terracotta: designed ICL loops; green: theozyme). Portrait layout. |
| `5_5.jpg` | 1932x334 | Figure 5.5 | `fig:sequence-design` | Sequence design comparison (gray: identical; red: mutated; green: theozyme positions) |
| `5_6.jpg` | 1471x1053 | Figure 5.6 | `fig:boltz2-evaluation` | Boltz2 evaluation (A: predicted structure overlay; B: catalytic geometry comparison; C: per-residue pLDDT) |

## Chapter 6 — ProtOS-MCP

| Source file | Dimensions | Thesis figure | Label | Description |
|-------------|-----------|---------------|-------|-------------|
| `6_1.jpg` | 1540x802 | Figure 6.1 | `fig:mcp-architecture` | ProtOS-MCP architecture sequence diagram (Scientist → AI → MCP → ProtOS, showing binding pocket comparison flow) |

## Unmapped files

| Source file | Dimensions | Note |
|-------------|-----------|------|
| `2_2.jpg` | 708x537 | Duplicate of `1_2.jpg` (retinal charge distribution, labeled "1.2"). Not used. |

## Missing figures (no image in zip)

| Label | Chapter | Description |
|-------|---------|-------------|
| `fig:mcp-conversation` | Ch6 | Complete MCP conversation (4 turns, redshifting the rhodozyme). Not included in zip. |
