# Discovery — py-Monocle3

## 1. Is the target already ported?

`gh repo view omicverse/py-Monocle3` → **not found at port start**.

A **comprehensive, well-maintained, parity-validated** community port exists: **[Bio-Babel/Monocle3-python](https://github.com/Bio-Babel/Monocle3-python)**.

The omicverse-rebuildr Phase 0.5 invariant says:
> "Is target already ported? → if YES: **stop, reuse existing repo**"

The Bio-Babel port is not under `omicverse/` but it is a fully-functional 1:1 port. The pragmatic decision is to **wrap it** under the omicverse namespace rather than re-port. This is what `pymonocle3` does: it re-exports the Bio-Babel `monocle3` package under the `pymonocle3` namespace.

## 2. R dependencies + py-mirror reuse

Reuse is delegated entirely to Bio-Babel/Monocle3-python:

| R dep | Bio-Babel handling | omicverse re-exposure |
|---|---|---|
| Matrix, S4Vectors, SingleCellExperiment | `anndata.AnnData` | ✅ |
| BiocGenerics, DelayedArray | (not used) | n/a |
| Rtsne / umap | umap-learn / openTSNE | ✅ |
| irlba (truncated SVD) | scipy.sparse.linalg.svds | ✅ |
| leidenbase | leidenalg | ✅ |
| monocle3-CR (C++ for SimplePPT) | pure Python | ✅ |
| RANN, FNN (kNN) | hnswlib | ✅ |
| ggplot2 | Bio-Babel/ggplot2-python | ✅ |
| pheatmap | Bio-Babel/pheatmap-python | ✅ |

## 3. Decision

**Wrap, not re-port** — the parity validation is *inherited* from Bio-Babel/Monocle3-python's own RECONSTRUCTION_REPORT. The omicverse port adds:
- A thin namespace re-export (`pymonocle3`)
- Documentation surfacing the inheritance
- Integration into the omicverse trajectory benchmark
- An omicverse-conformant deliverable set (this README, DISCOVERY, RECON_REPORT, etc.)
