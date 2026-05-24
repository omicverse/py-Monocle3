"""pymonocle3 — omicverse-facing wrapper for monocle3-python.

monocle3-python (https://github.com/Bio-Babel/Monocle3-python) is an excellent
Python port of R monocle3 by the Bio-Babel project. Rather than duplicate
their work, this package re-exports their full API under the omicverse
namespace + adds the omicverse-conformant parity-validation harness so the
downstream benchmarks treat it like the other ports.

Upstream: ``monocle3`` v1.4.26+. Install via::

    pip install monocle3-python   # transitive deps: hnswlib, leidenalg,
                                   # openTSNE, umap-learn, ...

R parity: ``learn_graph`` / ``order_cells`` / ``cluster_cells`` /
``preprocess_cds`` are all 1:1 re-implementations of the R monocle3
counterparts in monocle3-python. See their RECONSTRUCTION_REPORT.md for
details.

Use exactly the same API::

    import pymonocle3 as m3
    m3.preprocess_cds(adata, num_dim=50)
    m3.reduce_dimension(adata)
    m3.cluster_cells(adata)
    m3.learn_graph(adata)
    m3.order_cells(adata, root_pr_nodes=["Y_1"])
"""

from __future__ import annotations

import monocle3 as _m3
from monocle3 import *  # noqa: F401, F403 — re-export the full namespace

__version__ = "0.1.0"
__upstream_version__ = getattr(_m3, "__version__", "unknown")

# Explicitly re-export commonly used functions for IDE discoverability
from monocle3 import (
    preprocess_cds,
    align_cds,
    reduce_dimension,
    cluster_cells,
    learn_graph,
    order_cells,
    plot_cells,
    graph_test,
    top_markers,
    aggregate_gene_expression,
    find_gene_modules,
    pseudotime,
    principal_graph,
    clusters,
    partitions,
)

__all__ = [
    "preprocess_cds", "align_cds", "reduce_dimension",
    "cluster_cells", "learn_graph", "order_cells",
    "plot_cells", "graph_test", "top_markers",
    "aggregate_gene_expression", "find_gene_modules",
    "pseudotime", "principal_graph", "clusters", "partitions",
    "__version__", "__upstream_version__",
]
