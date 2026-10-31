# OptiProfiler 2.0 compatibility

This line is the reviewed RS13 adapter for OptiProfiler 2.0.0. Provider API
version remains **1**. Upstream problem definitions, selection metadata and the
automatic upstream-promotion policy are unchanged.

The adapter supplies selection and public Problem callbacks. Ordered feature
composition, counters and histories, scores, save/load, and eval_report/2 are
owned by core, not duplicated in adapters. No core-private class is accessed.
Python loaders return the exact public Problem class, not a subclass.

RS13 is the library behind the core's reference-driven profiles. 350 problems
carry an offline-verified record with the raw objective `fun`, the raw violation
`maxcv=0`, kind `feasible` and a source; a record never holds a precomputed
merit. These are best-known values, not proven optima. Each official solution
was evaluated through the actual adapter after strict dimension, finiteness and
exposed-bound checks, and had to repeat exactly and improve on the initial
point. Solution coordinates are not distributed, so `x_ref` stays absent.

The other 152 problems keep `reference=None` and the empirical default target:
`biggs5` and `problem2.1` lack dimension-matched solutions, and for 150 problems
the official value is no better than `f(x0)`. In 146 of those the official file
repeats the starting point, and plain local solvers reach far lower values on
some of them, so such a record would be a false target that every run passes at
its first evaluation.

Each normal load checks problem source, effective bounds and loader identity
before attaching the record, without additional oracle calls. Stale, missing and
malformed evidence means unknown. No new options are introduced. Core owns
feature propagation and reference-driven scoring.

The distribution version is 0.1.0 and it requires `optiprofiler>=2.0.0`, the
first core with the API-v1 plugin host; there is no upper cap. Neither is on
PyPI until it is released. Stable 1.3.5 is not an API-v1 plugin host, and the
earlier `>=1.4.0` was a placeholder, never a verified compatibility range.

Normal installation acceptance uses the full dependency resolver and pip
check. `--no-deps` or PYTHONPATH overrides do not pass that gate. Uninstall
removes this distribution only; separately managed runtime, cache and user data
remain untouched.

RS13 remains experimental. Its reviewed 502 runtime drivers are bundled;
solution and problemdata archives remain maintenance-only. The adapter code is
licensed under BSD-3-Clause; the upstream notices record permission for the
problem sources and are not a license grant for adapter code.
