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

This repository packages the OptiProfiler adapter together with the 502 Python
problem drivers from the official `rs13pm.zip` archive. The installed adapter
therefore loads ordinary RS13 problems without a separate runtime download.
Known-solution and upstream-audit archives remain external maintenance inputs.

## Package and Plugin

RS13 is an experimental external problem-library provider. The development
distribution name is `optiprofiler-rs13`; it installs `optiprofiler_rs13` and
registers this API-v1 entry point:

```toml
[project.entry-points."optiprofiler.problem_libraries"]
rs13 = "optiprofiler_rs13:get_problem_library"
```

The corresponding OptiProfiler release and this plugin distribution have not
been published yet. The `0.1.0` value in `pyproject.toml` is build metadata for
feature-branch wheel and source-distribution tests, not a release announcement.
RS13 is not an OptiProfiler core submodule and remains external.

For local development against a checked-out API-v1 OptiProfiler core:

```bash
python -m pip install -e /path/to/optiprofiler
python -m pip install -e . --no-deps --no-build-isolation
```

## Contents

- `rs13_tools.py`: public OptiProfiler adapter entry points and helper loaders.
- `runtime/rs13pm/`: the 502 vendored official Python problem drivers used by
  `rs13_load`.
- `probinfo_rs13.csv`: committed selection metadata used by `rs13_select`.
- `THIRD_PARTY_NOTICES.md`: exact upstream archive provenance, checksum,
  permission record, and citation.
- `scripts/collect_info.py`: regenerates `probinfo_rs13.csv` from local
  official archive extracts.
- `scripts/check_distribution.py`: verifies wheel/sdist runtime contents and
  excludes solution and audit data.
- `scripts/smoke_rs13.py`: small SciPy smoke runner for local sanity checks.
- `tests/test_rs13.py`: runtime wrapper tests for loading, selecting, committed
  metadata, known-solution evaluation, and the RS13 bound policy.
- `tests/test_upstream_data_audit.py`: maintenance-only comparison against the
  independent `problemdata` records.
- `docs/bound_role_policy.md`: explains why some official BAM search boxes are
  hidden from OptiProfiler.
- `docs/upstream_data_notes.md`: evidence notes for issues that can be reported
  upstream.

## Runtime and Maintenance Inputs

The distribution includes the 502 official Python drivers needed by
`rs13_load`. `rs13_check_available` verifies this bundled runtime, so ordinary
users do not download `rs13pm.zip` or set `RS13PM_DIR`. `rs13_select` reads the
committed `probinfo_rs13.csv` table.

Maintainers can explicitly test a reviewed upstream extract instead of the
bundled runtime by setting `RS13PM_DIR`. The lower-level `rs13_load_raw` and
`rs13_load_problem` helpers also accept an explicit `source_dir`. Resolution
order is explicit `source_dir`, then `RS13PM_DIR`, then the bundled runtime.

Two additional archives are test and maintenance inputs, not runtime,
distribution, or API-v1 protocol dependencies:

- `rs13sols.zip`: known solution vectors used as a test oracle and when
  regenerating `fbest` metadata.
- `problemdata.zip`: independent dimension, bound, and starting-point records
  used only by the upstream-data audit and metadata regeneration.

Maintainers can set these locations with environment variables:

```bash
# Optional override for reviewing a new rs13pm extract:
export RS13PM_DIR=/path/to/reviewed/rs13pm
# Optional test oracle:
export RS13SOLS_DIR=/path/to/rs13sols
# Maintenance audit only:
export RS13_PROBLEMDATA_DIR=/path/to/problemdata
```

The solution and problemdata helpers independently require only their own
inputs. No upstream assets are downloaded at import time or load time.

`RS13PM_DIR` is a maintainer override. `RS13SOLS_DIR` and
`RS13_PROBLEMDATA_DIR` are test and maintenance locations. None is a benchmark
`plib_option`: the plugin intentionally declares no library-specific options,
and nonempty `plib_options={"rs13": ...}` mappings are rejected.

## Usage

```python
from optiprofiler_rs13 import rs13_load, rs13_select

names = rs13_select({"ptype": "u", "maxdim": 10})
problem = rs13_load(names[0])
print(problem.name, problem.ptype, problem.fun(problem.x0))
```

In OptiProfiler, use this adapter as the problem library `rs13`, for example:

```python
from optiprofiler import benchmark

benchmark(solvers, plibs=["rs13"])
```

An installed plugin needs no filesystem path. Discovery also reads entry-point
metadata without loading the upstream archive:

```python
from optiprofiler import list_problem_libraries

assert "rs13" in list_problem_libraries()
```

## Update and Uninstall

Keep two update operations separate:

1. update the unpublished adapter, its reviewed vendored `rs13pm` snapshot,
   and its provenance record on the compatible feature branch;
2. update the external `rs13sols` and `problemdata` maintenance inputs only
   when running the corresponding checks.

```bash
git pull --ff-only
python -m pip install -e . --no-deps --no-build-isolation
```

The tested adapter commit is recorded by the OptiProfiler core
`problem_libraries.lock`. Installing a newer adapter changes the bundled
runtime snapshot together with the wrapper. It does not download or alter
external `rs13sols`, `problemdata`, maintainer override directories, or
benchmark results.

Remove only the experimental adapter and its entry point with:

```bash
python -m pip uninstall optiprofiler-rs13
```

This removes the adapter, entry point, bundled runtime, and bundled metadata.
It preserves any separately managed `RS13PM_DIR`, `RS13SOLS_DIR`,
`RS13_PROBLEMDATA_DIR`, maintenance inputs, caches, and benchmark output.
Removing the OptiProfiler core leaves this independent adapter and its bundled
runtime installed; the adapter remains unusable until a compatible core is
reinstalled.

## Public API

The user-facing entry points are:

- `rs13_load(problem_name)`: loads one RS13 scalar objective as an
  OptiProfiler `Problem`.
- `rs13_select(options)`: returns RS13 problem names satisfying
  OptiProfiler-style filters such as `ptype`, `mindim`, `maxdim`, `minb`,
  `maxb`, `mincon`, `maxcon`, and `excludelist`.
- `rs13_collect_info(...)`: reads or regenerates the committed
  `probinfo_rs13.csv` table.
- `rs13_check_available()`: verifies that the selected bundled or override
  runtime contains all 502 official Python drivers before a benchmark starts.

Additional test and maintenance helpers:

- `rs13_load_raw(problem_name)`: loads the objective, starting point, and
  official BAM-driver bounds from one `rs13pm` Python file.
- `rs13_known_solution(problem_name)`: reads a known solution test oracle from
  `rs13sols.zip` extracts; it is not used by `rs13_load`.
- `rs13_problemdata(problem_name)`: reads official dimension, bounds, and
  starting point from `problemdata.zip` extracts for maintenance audits.

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

The main CI workflow runs on pushes, pull requests, manual dispatch, and daily
at 07:00 Beijing time. It validates the API-v1 plugin, builds both distribution
formats, confirms that both contain exactly 502 runtime drivers, and exercises
the source checkout and a fresh wheel installation with every `RS13*`
environment variable unset. It downloads only the `rs13sols` test oracle for
known-solution and solver smoke checks. It does not download `rs13pm` or
`problemdata`, or regenerate metadata.

The separate `Upstream Data Audit` workflow runs on a daily schedule and manual
dispatch only. It downloads all three official archives, runs
`tests/test_upstream_data_audit.py`, regenerates `probinfo_rs13.csv`, and fails
visibly if the independent upstream records are unavailable or have changed.
It does not run on pushes or pull requests and therefore does not make upstream
website availability a plugin regression signal.

Run the wrapper tests from this repository:

```bash
python -m unittest discover -s tests -p 'test_rs13.py'
python -m unittest discover -s tests -p 'test_plugin_protocol.py'
```

Run the upstream-data audit after setting all three maintenance inputs:

```bash
python -m unittest discover -s tests -p 'test_upstream_data_audit.py'
python scripts/collect_info.py
git diff --exit-code probinfo_rs13.csv
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

1. download `rs13pm.zip` from the documented upstream URL and verify the
   reviewed archive checksum;
2. replace `runtime/rs13pm/` with exactly its 502 Python drivers and update
   `THIRD_PARTY_NOTICES.md`;
3. keep separate extracts of `rs13sols` and `problemdata`, then set
   `RS13PM_DIR=runtime/rs13pm`, `RS13SOLS_DIR`, and
   `RS13_PROBLEMDATA_DIR`;
4. run `python scripts/collect_info.py`, the upstream-data audit, runtime tests,
   build, and `python scripts/check_distribution.py`;
5. review source, provenance, metadata, and archive-content diffs before
   committing.

Do not commit archive ZIPs, `rs13sols`, `problemdata`, BAM executables,
benchmark outputs, or local cache/build artifacts.

## Provenance and Citation

The vendored `rs13pm.zip` archive did not include a standalone `LICENSE`,
`LICENCE`, `COPYING`, or `NOTICE` file, and its Python files did not carry an
open-source license header. Professor Nikolaos V. Sahinidis confirmed by email
on 2026-06-27 that the RS13 collection is in the open domain and may be used in
the OptiProfiler integration model described to him. See
`THIRD_PARTY_NOTICES.md` for the exact vendored source URL, retrieval date,
archive checksum, and distribution boundary.

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
