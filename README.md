# RS13 Adapter

OptiProfiler adapter for the Rios-Sahinidis 2013 derivative-free optimization
test set.

RS13 contains 502 continuous nonlinear black-box optimization problems from
Rios and Sahinidis, *Derivative-free optimization: A review of algorithms and
comparison of software implementations*, Journal of Global Optimization, 56,
1247-1293, 2013. The official Georgia Tech page provides the original paper
context, problem sources, solver results, and problem statistics:

- https://sahinidis.coe.gatech.edu/dfo
- https://sahinidis.coe.gatech.edu/comp

The Optimization Firm also provides RS13 files for BAM-facing Python/C/Fortran
interfaces, BAM input files, known solutions, and executable bundles:

- https://minlp.com/black-box-optimization-test-problems

This repository adds only the OptiProfiler adapter, generated metadata, tests,
and documentation. It does not vendor the official RS13 source archives.

## Contents

- `rs13_tools.py`: public OptiProfiler adapter entry points and helper loaders.
- `probinfo_rs13.csv`: committed selection metadata used by `rs13_select`.
- `scripts/collect_info.py`: regenerates `probinfo_rs13.csv` from local
  official archive extracts.
- `scripts/smoke_rs13.py`: small SciPy smoke runner for local sanity checks.
- `tests/test_rs13.py`: wrapper-level tests for loading, selecting, metadata,
  known-solution evaluation, and the RS13 bound policy.
- `docs/bound_role_policy.md`: explains why some official BAM search boxes are
  hidden from OptiProfiler.
- `docs/upstream_data_notes.md`: evidence notes for issues that can be reported
  upstream.

## Upstream Inputs

Download and extract these official RS13 archives before running
`rs13_load`, regenerating metadata, or running the full tests:

- `rs13pm.zip`: Python files using BAM's SciPy-style API.
- `rs13sols.zip`: known solution vectors.
- `problemdata.zip`: dimensions, bounds, and starting points.

Set the archive locations with environment variables:

```bash
export RS13PM_DIR=/path/to/rs13pm
export RS13SOLS_DIR=/path/to/rs13sols
export RS13_PROBLEMDATA_DIR=/path/to/problemdata
```

The adapter intentionally fails clearly if these paths are missing. It does not
silently download upstream assets at import time or load time.

## Usage

```python
from rs13_tools import rs13_load, rs13_select

names = rs13_select({"ptype": "u", "maxdim": 10})
problem = rs13_load(names[0])
print(problem.name, problem.ptype, problem.fun(problem.x0))
```

In OptiProfiler, use this adapter as the problem library `rs13`, for example:

```python
benchmark(solvers, plibs=["rs13"], custom_problem_libs_path="/path/to/problem_libs")
```

## Public API

The user-facing entry points are:

- `rs13_load(problem_name)`: loads one RS13 scalar objective as an
  OptiProfiler `Problem`.
- `rs13_select(options)`: returns RS13 problem names satisfying
  OptiProfiler-style filters such as `ptype`, `mindim`, `maxdim`, `minb`,
  `maxb`, `mincon`, `maxcon`, and `excludelist`.
- `rs13_collect_info(...)`: reads or regenerates the committed
  `probinfo_rs13.csv` table.

Additional maintenance helpers:

- `rs13_load_raw(problem_name)`: loads the objective, starting point, and
  official BAM-driver bounds from one `rs13pm` Python file.
- `rs13_known_solution(problem_name)`: reads the known solution vector from
  `rs13sols.zip` extracts.
- `rs13_problemdata(problem_name)`: reads official dimension, bounds, and
  starting point from `problemdata.zip` extracts.

## Problem Metadata

`probinfo_rs13.csv` follows the same broad convention as the other
OptiProfiler problem-library metadata tables. It contains fixed-size rows with
fields such as `problem_name`, `ptype`, `xtype`, `dim`, `mb`, `ml`, `mu`,
`mcon`, `mlcon`, `mnlcon`, `f0`, `fbest`, `source_file`,
`problemdata_status`, and `known_solution_status`.

RS13 does not expose variable-size constructors through adapter arguments.
Each official RS13 source file corresponds to one fixed problem, so this table
does not include S2MPJ-style `argins`, `dims`, `mbs`, or `f0s` columns.

The known solutions are currently used only to compute lightweight metadata
such as `fbest` and to validate the wrapper in tests. Solvers do not receive
these solution vectors through `rs13_load`. They may be useful later for
benchmark diagnostics, validation, or quality checks.

## Bound Policy

RS13's public Python files are BAM driver scripts. BAM is a box-partitioning
solver, so those files attach finite `xmin`/`xmax` search boxes even to
problems whose mathematical definitions are unconstrained.

The adapter therefore distinguishes official BAM-driver bounds from the bounds
exposed to OptiProfiler:

- 371 source-reviewed search-box-only problems are exposed as unconstrained
  (`ptype = u`, `mb = 0`).
- 131 problems preserve their finite bounds (`ptype = b`) because the bounds
  appear intrinsic, domain-protective, bound-active, or unresolved.

For example, `rosenbr` and the generated `convex1`/`convex2`/`convex3`/
`convex4` families are treated as unconstrained even though the BAM driver
uses large boxes such as `[-10000, 10000]`. Problems such as `3pk`,
`hatflda`, `logros`, and `problem3.13` keep bounds because source-level review
found nonnegative/domain bounds or a risk of unboundedness after removing the
lower bounds.

See `docs/bound_role_policy.md` for the detailed policy and preserved-case
notes.

## Upstream Data Notes

`docs/upstream_data_notes.md` records the issues currently worth reporting to
the upstream maintainers:

- `biggs5`: known-solution vector length does not match the problem dimension.
- `problem2.1`: known-solution vector length does not match the problem
  dimension.
- `problem3.15`: `problemdata` starting-point row appears to have one missing
  entry.
- `median`: collection label appears suspicious (`princetonlinb`).
- `ex8_1_6` and `st_e39`: source-level models appear very similar and may be
  aliases or duplicates.

The adapter does not guess corrections for these. It records status fields in
`probinfo_rs13.csv` and uses the official Python wrapper data when available.

## Testing

The CI workflow runs on pushes, pull requests, manual dispatch, and daily at
07:00 Beijing time. It downloads the official RS13 archives, installs
OptiProfiler, runs wrapper tests, checks that regenerated metadata is
committed, and runs the smoke script.

Run the wrapper tests from this repository:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Regenerate the metadata table from local official archive extracts:

```bash
python scripts/collect_info.py
```

Run a small local smoke check:

```bash
python scripts/smoke_rs13.py
```

## Maintenance

When upstream RS13 assets change:

1. download the official archives from the upstream pages;
2. set `RS13PM_DIR`, `RS13SOLS_DIR`, and `RS13_PROBLEMDATA_DIR`;
3. run `python scripts/collect_info.py`;
4. run the tests;
5. review any metadata diff before committing.

The repository should stay adapter-only and lightweight. Do not commit
downloaded upstream archives, extracted RS13 source trees, BAM executables,
benchmark output directories, or local cache/build artifacts.

## Provenance and Citation

The checked archives did not include a standalone `LICENSE`, `LICENCE`,
`COPYING`, or `NOTICE` file, and sampled Python/C/Fortran/BAM/problemdata files
did not carry an open-source license header. Professor Nikolaos V. Sahinidis
confirmed by email on 2026-06-27 that the RS13 collection is in the open domain
and may be used in the OptiProfiler integration model described to him.

Please cite the original paper and link to the upstream pages when using RS13
through this adapter:

```text
L. M. Rios and N. V. Sahinidis,
Derivative-free optimization: A review of algorithms and comparison of
software implementations,
Journal of Global Optimization, 56, 1247-1293, 2013.
https://doi.org/10.1007/s10898-012-9951-y
```

Upstream source pages:

- https://sahinidis.coe.gatech.edu/dfo
- https://sahinidis.coe.gatech.edu/comp
- https://minlp.com/black-box-optimization-test-problems
