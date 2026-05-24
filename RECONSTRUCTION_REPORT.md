# Reconstruction Report — py-Monocle3 v0.1.0

## 1. Identity

| Field | Value |
|---|---|
| Python package | `pymonocle3` (PyPI dist `pymonocle3-bio`) |
| Upstream R package | `monocle3` v1.4.x |
| Upstream Python port | **Bio-Babel/Monocle3-python** v1.4.26+ (the actual ported code) |
| Citation | Cao et al. *Nature* 2019; Trapnell et al. *Nat Biotech* 2014 |
| Algorithm class | (multi-output) |
| Parity strategy | **wrapper — inherited from Bio-Babel/Monocle3-python** |
| LOC | ~50 Python (wrapper only) |

## 2. R function coverage audit

Inherited. Every function listed in [`examples/function_by_function_R_parity.ipynb`](examples/function_by_function_R_parity.ipynb) is re-exported and verified `pymonocle3.<fn> is monocle3.<fn>` (Bio-Babel object identity check).

## 3. Parity evidence

Inherited from Bio-Babel/Monocle3-python. See their tutorials reproducing R monocle3 vignettes on the Packer 2019 *C. elegans* embryo and Cao 2017 L2 datasets.

## 4. Acceleration evidence

None added by wrapper.

## 5. Code quality

| Check | Status |
|---|---|
| `pip install pymonocle3-bio` | ✅ (pulls in monocle3-python) |
| `pytest -q` | ✅ 2/2 (import + tiny pipeline) |
| 4 notebooks executed | ✅ |
| README + MATH + DISCOVERY + this report | ✅ |
| Version 0.1.0 | ✅ |

## 6. Known limitations

The wrapper itself adds nothing; all limitations are those of Bio-Babel/Monocle3-python upstream. As of v1.4.26 those are:

- See <https://github.com/Bio-Babel/Monocle3-python#status> for the live limitation list.

## 7. omicverse integration

- `omicverse.external.pymonocle3` (planned alias)
- This was a **wrap-don't-rebuild** decision per the rebuildr Phase 0.5 invariant.

## 8. Sign-off

| Field | Value |
|---|---|
| Author | claude-opus-4-7 via omicverse-rebuildr |
| Date | 2026-05-24 |
| Audit class | A (inherited) |
