"""Smoke test: import + smallest end-to-end pipeline."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_import():
    import pymonocle3
    assert pymonocle3.__version__ == "0.1.0"
    assert hasattr(pymonocle3, "preprocess_cds")
    assert hasattr(pymonocle3, "learn_graph")
    assert hasattr(pymonocle3, "order_cells")


def test_pipeline_on_tiny_synth():
    import numpy as np
    import anndata as ad
    import pymonocle3 as m3

    rng = np.random.RandomState(0)
    n_cells = 60
    n_genes = 80
    counts = rng.poisson(2.0, (n_cells, n_genes)).astype(float)
    # add a smooth gradient in 10 of the genes to give learn_graph a signal
    pt = np.linspace(0, 1, n_cells)
    counts[:, :10] += rng.poisson(20 * pt[:, None], (n_cells, 10))

    adata = ad.AnnData(X=counts)
    adata.obs_names = [f"cell_{i}" for i in range(n_cells)]
    adata.var_names = [f"gene_{i}" for i in range(n_genes)]

    m3.preprocess_cds(adata, num_dim=10)
    m3.reduce_dimension(adata, max_components=2, umap_min_dist=0.1)
    m3.cluster_cells(adata)
    m3.learn_graph(adata)
    assert "principal_graph" in adata.uns or hasattr(adata, "obsp")
