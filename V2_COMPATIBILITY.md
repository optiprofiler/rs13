# OptiProfiler 2.0 compatibility candidate

This branch is an unpushed compatibility candidate, not a release. Provider
API version remains **1**. No adapter version, upstream problem definitions,
selection metadata, or automatic upstream-promotion policy is changed.

The adapter supplies selection and public Problem callbacks. Ordered feature
composition, counters and histories, scores, save/load, and eval_report/2 are
owned by core, not duplicated in adapters. No core-private class is accessed.
Python loaders return the exact public Problem class, not a subclass.

The candidate promotes 500 offline-verified feasible scalar records, with
kind `best_known` and mapping `feasible_objective/1`. They are not proven
optima. The official solution coordinates were evaluated through the actual
adapter twice after strict dimension, finiteness and exposed-bound checks;
coordinates are not distributed. `biggs5` and `problem2.1` lack valid
dimension-matched evidence and retain `reference=None`.

Each normal load checks problem source, effective bounds and loader identity
before attaching the public record, without additional oracle calls. Stale,
missing and malformed evidence means unknown. No new options are introduced.
Core owns safe/unsafe feature propagation and any eventual profile consumption;
this provider change alone does not implement reference-based scoring.

The proposed first compatible distribution version is 0.1.0, not yet
published. This candidate requires OptiProfiler >=2.0.0. Stable 1.3.5 is not
an API-v1 plugin host; the previous >=1.4.0 was a future placeholder, not a
verified released compatibility range.

Normal installation acceptance uses the full dependency resolver and pip
check. Before public 2.0 exists, use an explicitly labelled private candidate
wheelhouse. --no-deps or PYTHONPATH overrides do not pass that gate. Existing
development CI shortcuts are contract tests, not normal-install acceptance.
Uninstall removes this distribution only; separately managed runtime, cache
and user data remain untouched.

RS13 remains experimental. Its reviewed 502 runtime drivers are bundled;
solution and problemdata archives remain maintenance-only. Current notices
record upstream permission, not a new license grant for our adapter code.
Final distribution license metadata requires owner review before release.
