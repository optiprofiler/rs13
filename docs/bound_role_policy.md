# RS13 Bound-Role Policy

RS13's public Python files are BAM driver scripts. BAM is a box-partitioning
method, so the driver scripts provide finite `xmin`/`xmax` values even for
problems whose mathematical definitions are unconstrained. The OptiProfiler
adapter therefore distinguishes:

- **official RS13/BAM bounds**: the finite search box used by the RS13 driver;
- **adapter bounds**: the bounds exposed to OptiProfiler solvers.

After source-level review, the adapter strips search-box-only bounds for 371
problems and exposes them as unconstrained (`ptype = u`). It preserves bounds
for 131 problems.

## Evidence Used

The review used:

- official RS13 Python driver files from `rs13pm.zip`;
- official `problemdata.zip` and `rs13sols.zip`;
- the official comparison table `comp.html`;
- Princeton/Global source files where available;
- Luksan-Vlcek Fortran source files where available;
- wrapper-level checks that `probinfo_rs13.csv` and `rs13_load` expose the same
  effective problem type and bound count.

Official source pages:

- https://sahinidis.coe.gatech.edu/dfo
- https://sahinidis.coe.gatech.edu/comp
- https://minlp.com/black-box-optimization-test-problems

Typical evidence for stripping bounds is: the original source has no finite
variable bounds, while the RS13 Python driver only adds a large BAM search box
such as `[-10000, 10000]`. Classic examples include `rosenbr` and the generated
`convex1`/`convex2`/`convex3`/`convex4` families.

## Preserved Suspicious Cases

The first-pass heuristic marked 410 problems as likely search-box cases. A
manual/source-level review found that the following 39 should not be stripped
for now:

- `3pk`: original source has nonnegative lower bounds.
- `allinit`: original source has one-sided finite bounds.
- `biggs6`: original source has finite bounds on part of the variables.
- `denschna`, `denschnc`, `denschne`, `expfit`: finite bounds protect
  exponential parameters in the source-level problem.
- `emfl_vareps`, `hatflda`, `logros`: finite lower bounds encode domain or
  regularization constraints.
- `ex4_1_5`, `least`: source-level finite bounds are not pure BAM boxes.
- `hs001`, `osbornea`, `palmer1`, `palmer1e`, `palmer2a`, `palmer2e`,
  `palmer3`, `palmer3e`, `palmer4`, `palmer4e`, `palmer5a`, `palmer5b`,
  `palmer5e`, `palmer6a`, `palmer6e`, `palmer7e`, `palmer8a`, `palmer8e`,
  `penalty2`, `qr3dls`, `s257`, `s259`, `s261`, `s272`, `s333`, `yfit`:
  original source contains finite bounds.
- `problem3.13`: removing the nonnegative lower bounds appears to make the
  problem unbounded below.

## Data Caveats

- `problem3.15` is exposed as unconstrained because its bounds appear to be
  search-box-only, but its official `problemdata` file has a 5-entry starting
  point row for a 6-dimensional problem. This remains an upstream data issue.
- `median` is exposed as unconstrained, but its collection label
  `princetonlinb` appears suspicious and should be confirmed upstream.
- `ex8_1_6` and `st_e39` appear very similar in the source-level model and may
  be duplicate/alias entries.

## Adapter Rule

The authoritative behavior lives in `rs13_tools.py`:

- names with prefixes `convex1_`, `convex2_`, `convex3_`, and `convex4_` are
  exposed as unconstrained;
- additional source-reviewed search-box-only names are listed in
  `RS13_EFFECTIVE_UNCONSTRAINED_NAMES`;
- all other RS13 problems preserve their official bounds.

The committed `probinfo_rs13.csv` table is generated from this adapter policy.
For each row, `ptype` and `mb` should match the `Problem.ptype` and
`Problem.mb` returned by `rs13_load`.
