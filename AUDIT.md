# AUDIT — py-Monocle3

Coverage is **inherited from Bio-Babel/Monocle3-python**. The omicverse wrapper imports the full namespace via `from monocle3 import *`; every public function is therefore reachable as `pymonocle3.<fn>` and is the same Python object as `monocle3.<fn>` (verified in `examples/compare_R_vs_Python.ipynb` §1).

## R function → Python mapping (selected)

| R `monocle3::<fn>` | Python `pymonocle3.<fn>` | Status |
|---|---|---|
| `new_cell_data_set` | `anndata.AnnData` (replacement) | ✅ |
| `estimate_size_factors` | `estimate_size_factors` | ✅ |
| `preprocess_cds` | `preprocess_cds` | ✅ |
| `align_cds` | `align_cds` | ✅ |
| `reduce_dimension` | `reduce_dimension` | ✅ |
| `cluster_cells` | `cluster_cells` | ✅ |
| `learn_graph` | `learn_graph` | ✅ |
| `order_cells` | `order_cells` | ✅ |
| `pseudotime`, `principal_graph`, `clusters`, `partitions` | same names | ✅ |
| `graph_test` | `graph_test` | ✅ |
| `top_markers` | `top_markers` | ✅ |
| `find_gene_modules` | `find_gene_modules` | ✅ |
| `aggregate_gene_expression` | `aggregate_gene_expression` | ✅ |
| `plot_cells`, `plot_cells_3d` | same names | ✅ |
| `transfer_cell_labels`, `fix_missing_cell_labels` | same names | ✅ |

Full list: see `pymonocle3.__all__` and the Bio-Babel/Monocle3-python `monocle3/__init__.py`.

## Coverage statistics (inherited)

Refer to <https://github.com/Bio-Babel/Monocle3-python#coverage> for the live coverage table. As of v1.4.26 it covers all exported R monocle3 functions used in the standard tutorial vignettes.
