"""OptiProfiler adapter for the RS13 derivative-free optimization test set."""

from .rs13_tools import (
    RS13_SMOKE_PROBLEMS,
    RS13ProblemSource,
    rs13_check_available,
    rs13_collect_info,
    rs13_known_solution,
    rs13_load,
    rs13_load_problem,
    rs13_load_raw,
    rs13_problemdata,
    rs13_select,
)


def _plugin_select(problem_options, library_options):
    return rs13_select(problem_options, library_options=library_options)


def _plugin_load(problem_name, library_options):
    return rs13_load(problem_name, library_options=library_options)


def get_problem_library():
    """Return the experimental OptiProfiler API-v1 plugin for RS13."""

    from optiprofiler import ProblemLibraryPlugin

    return ProblemLibraryPlugin(
        name="rs13",
        api_version=1,
        select=_plugin_select,
        load=_plugin_load,
        collect_info=rs13_collect_info,
        check_available=rs13_check_available,
    )

__all__ = [
    "RS13_SMOKE_PROBLEMS",
    "RS13ProblemSource",
    "get_problem_library",
    "rs13_check_available",
    "rs13_collect_info",
    "rs13_known_solution",
    "rs13_load",
    "rs13_load_problem",
    "rs13_load_raw",
    "rs13_problemdata",
    "rs13_select",
]
