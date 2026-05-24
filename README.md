# py-Monocle3

omicverse-facing wrapper for [**Bio-Babel/Monocle3-python**](https://github.com/Bio-Babel/Monocle3-python) — a comprehensive Python port of R monocle3 (Cao et al. *Nature* 2019 / Trapnell et al. *Nat Biotech* 2014).

Rather than duplicate Bio-Babel's excellent work, this package re-exports their full API under the `pymonocle3` namespace + adds omicverse-conformant parity-validation harness so the trajectory benchmark treats it like the other ports.

## Install

```bash
pip install pymonocle3-bio
```

This pulls in `monocle3-python` + its transitive deps (`hnswlib`, `leidenalg`, `openTSNE`, `umap-learn`, `pheatmap-python`, `igraph`).

## Quick-start

```python
import pymonocle3 as m3

adata = m3.load_packer_embryo()
m3.preprocess_cds(adata, num_dim=50)
m3.reduce_dimension(adata)
m3.cluster_cells(adata)
m3.learn_graph(adata)
m3.order_cells(adata, root_pr_nodes=["Y_1"])
m3.plot_cells(adata, color_cells_by="pseudotime")
```

## Function coverage

This package re-exports the full Bio-Babel/Monocle3-python API:

- `preprocess_cds`, `align_cds`, `reduce_dimension`, `cluster_cells`
- `learn_graph`, `order_cells`, `pseudotime`, `principal_graph`
- `graph_test`, `top_markers`, `find_gene_modules`, `aggregate_gene_expression`
- `plot_cells`, `plot_cells_3d`
- `transfer_cell_labels`, `fix_missing_cell_labels`
- All accessors / projections / data loaders

See [Bio-Babel/Monocle3-python](https://github.com/Bio-Babel/Monocle3-python) for the full R parity report.

## License

Artistic-2.0, matching upstream monocle3 / monocle3-python.

## Citation

> Cao, J. et al. *The single-cell transcriptional landscape of mammalian organogenesis.* Nature 566, 496–502 (2019).
> Trapnell, C. et al. *The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells.* Nat Biotechnol 32, 381–386 (2014).
