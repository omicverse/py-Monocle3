# py-Monocle3 — Math Notes (inherited)

This package is a thin wrapper around **Bio-Babel/Monocle3-python**, which has its own MATH.md documenting algorithmic choices, perturbation bounds, and divergence from R monocle3.

Cross-reference: <https://github.com/Bio-Babel/Monocle3-python/blob/main/MATH.md> (if present) or the per-module docstrings inside the `monocle3` package.

## 1. Bit-equivalent (E)

Inherited from upstream; pymonocle3 introduces no new numerical paths.

## 2. Bounded ε-approximations (B)

None added by the wrapper. Upstream's bounds (if any) apply.

## 3. Class-containment (C)

None added by the wrapper.

## 4. Wrapper-introduced divergence

**None.** Every public function in `pymonocle3.*` is `is` the same Python object as `monocle3.*` (verified in `examples/compare_R_vs_Python.ipynb` §1).

## 5. Audit class

**A — translation-only**, by inheritance from upstream.
