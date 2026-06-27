# RS13 Upstream Data Notes

This note records small data inconsistencies and source-level questions
observed while building the OptiProfiler RS13 problem-library adapter. It is
intended as a neutral reference for a possible upstream report.

Checked date: 2026-06-27.

Official archive families used for the check:

- `rs13pm.zip`: Python files using BAM's SciPy-style API.
- `rs13sols.zip`: known solution vectors.
- `problemdata.zip`: dimension, bound, and starting-point records.
- `rs13c.zip`: C source/API files.
- `rs13src.zip`: Fortran source files.

Official source pages:

- https://sahinidis.coe.gatech.edu/dfo
- https://sahinidis.coe.gatech.edu/comp
- https://minlp.com/black-box-optimization-test-problems

## Summary

The generated OptiProfiler metadata currently contains 502 RS13 problems.
Known solution vectors are dimension-consistent for 500 of them. Two solution
files have a vector length that does not match the corresponding Python
problem and `problemdata` dimension:

- `biggs5`: solution vector has 6 entries, while the problem dimension is 5.
- `problem2.1`: solution vector has 3 entries, while the problem dimension is 2.

One `problemdata` file appears to have an incomplete starting-point row:

- `problem3.15`: `problemdata` declares dimension 6, but its starting-point row
  has 5 entries. The Python, C, Fortran, and solution-vector files all indicate
  dimension 6.

Two source/statistics questions are also worth asking upstream:

- `median`: the collection label appears as `princetonlinb`; this may be a
  typo for `princetonlib`, but it should be confirmed.
- `ex8_1_6` and `st_e39`: the source-level models and metadata appear very
  similar, possibly aliases or duplicate entries.

The OptiProfiler RS13 adapter does not guess corrections. It marks the two
solution-vector mismatches as missing known solutions in `probinfo_rs13.csv`
and uses the Python wrapper data for `problem3.15`.

## Details

### `biggs5`

Observed files:

- `rs13pm/biggs5.py`
  - `xmin = [-100, -100, -10000, -10000, -100]`
  - `xmax = [100, 100, 10000, 10000, 100]`
  - `x0 = [0, 0, 0, 0, 0]`
- `problemdata/biggs5.problem.data`
  - declared dimension: `5`
  - lower-bound row: 5 entries
  - upper-bound row: 5 entries
  - starting-point row: 5 entries
- `rs13sols/biggs5.sol`
  - solution vector: `10 1 -5 -1 4 3`
  - vector length: 6

Current metadata row:

```text
biggs5,b,r,5,10,5,5,0,0,0,0,0,0,0,0,0,66.424430264082943,nan,0,0,0,0,0,0,0,0,biggs5.py,ok,dimension_mismatch:6!=5
```

Question for upstream: should `biggs5.sol` contain a 5-dimensional vector, or
does one of the problem definitions miss a sixth variable?

### `problem2.1`

Observed files:

- `rs13pm/problem2.1.py`
  - objective reads two variables from `xin`
  - `xmin = [-50, -50]`
  - `xmax = [50, 50]`
  - `x0 = [0, 0]`
- `problemdata/problem2.1.problem.data`
  - declared dimension: `2`
  - lower-bound row: 2 entries
  - upper-bound row: 2 entries
  - starting-point row: 2 entries
- `rs13sols/problem2.1.sol`
  - solution vector: `0.328819 0.000000 0.131418`
  - vector length: 3

Current metadata row:

```text
problem2.1,b,r,2,4,2,2,0,0,0,0,0,0,0,0,0,8,nan,0,0,0,0,0,0,0,0,problem2.1.py,ok,dimension_mismatch:3!=2
```

Question for upstream: is the third value in `problem2.1.sol` intended to be
something other than a decision variable, such as an objective value or another
reported quantity?

### `problem3.15`

Observed files:

- `rs13pm/problem3.15.py`
  - objective reads 6 variables
  - `xmin = [-5000, -20, -5000, -5000, -5000, -20]`
  - `xmax = [10000, 30, 10000, 10000, 10000, 30]`
  - `x0 = [0, 0, 0, 0, 0, 0]`
- `rs13c/problem3.15.c`
  - `int nvars = 6`
  - `double xmin[6] = {-5000, -20, -5000, -5000, -5000, -20}`
  - `double xmax[6] = {10000, 30, 10000, 10000, 10000, 30}`
- `rs13src/problem3.15.f`
  - declares `double precision x(6)`
  - reads `x(1)` through `x(6)`
- `rs13sols/problem3.15.sol`
  - solution vector has 6 entries
- `problemdata/problem3.15.problem.data`
  - declared dimension: `6`
  - lower-bound row: 6 entries
  - upper-bound row: 6 entries
  - starting-point row: `0 0 0 0 0`
  - starting-point row length: 5

Current metadata row:

```text
problem3.15,u,r,6,0,0,0,0,0,0,0,0,0,0,0,0,8.02100361066862,0.55981567827684875,1,0,0,0,0,0,0,0,problem3.15.py,mismatch,ok
```

Question for upstream: should the starting-point row in
`problem3.15.problem.data` be `0 0 0 0 0 0`?

### `median`

Observed files:

- `rs13pm/median.py`
  - scalar one-dimensional objective
  - official BAM-driver bounds are `[-10000, 10000]`
- official comparison/statistics table
  - collection label: `princetonlinb`

Current metadata row:

```text
median,u,r,1,0,0,0,0,0,0,0,0,0,0,0,0,9.3353900869000004,4.9424198310999987,1,0,0,0,0,0,0,0,median.py,ok,ok
```

Question for upstream: is `princetonlinb` the intended collection label for
`median`, or should it be `princetonlib`?

### `ex8_1_6` and `st_e39`

Observed files:

- `rs13pm/ex8_1_6.py`
- `rs13pm/st_e39.py`
- official metadata gives both problems the same dimension and the current
  adapter computes the same `f0` and `fbest` values for both.

Current metadata rows:

```text
ex8_1_6,u,r,2,0,0,0,0,0,0,0,0,0,0,0,0,-0.49349841453301291,-10.086001344158241,1,0,0,0,0,0,0,0,ex8_1_6.py,ok,ok
st_e39,u,r,2,0,0,0,0,0,0,0,0,0,0,0,0,-0.49349841453301291,-10.086001344158241,1,0,0,0,0,0,0,0,st_e39.py,ok,ok
```

Question for upstream: are `ex8_1_6` and `st_e39` intentionally separate
entries, aliases of the same model, or an accidental duplicate?

## Reproduction Snippets

Count the solution-vector lengths:

```bash
wc -w rs13sols/biggs5.sol rs13sols/problem2.1.sol rs13sols/problem3.15.sol
```

Check the declared dimension and starting-point-row length in `problemdata`:

```bash
awk 'FNR==1{print FILENAME, "declared_n=" $1, "fields=" NF} FNR==4{print FILENAME, "x0_fields=" NF, $0}' \
  problemdata/biggs5.problem.data \
  problemdata/problem2.1.problem.data \
  problemdata/problem3.15.problem.data
```

Check the generated OptiProfiler metadata rows:

```bash
rg -n "^(biggs5|problem2\\.1|problem3\\.15|median|ex8_1_6|st_e39)," probinfo_rs13.csv
```
