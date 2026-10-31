from pathlib import Path
import json
import tarfile
from zipfile import ZipFile


EXPECTED_RUNTIME_FILES = 502


def _member_names(path: Path) -> list[str]:
    if path.suffix == ".whl":
        with ZipFile(path) as archive:
            return archive.namelist()
    with tarfile.open(path, "r:gz") as archive:
        return archive.getnames()


def _check_archive(path: Path) -> None:
    names = _member_names(path)
    runtime_files = [
        name
        for name in names
        if "/runtime/rs13pm/" in f"/{name}" and name.endswith(".py")
    ]
    if len(runtime_files) != EXPECTED_RUNTIME_FILES:
        raise AssertionError(
            f"{path.name} contains {len(runtime_files)} RS13 runtime files; "
            f"expected {EXPECTED_RUNTIME_FILES}."
        )

    required_suffixes = (
        "/probinfo_rs13.csv",
        "/LICENSE",
        "/THIRD_PARTY_NOTICES.md",
        "/UPSTREAM_SNAPSHOT.json",
        "/references.json",
        "/rs13_reference.py",
        "/runtime/rs13pm/branin.py",
        "/runtime/rs13pm/rosenbr.py",
    )
    for suffix in required_suffixes:
        if not any(f"/{name}".endswith(suffix) for name in names):
            raise AssertionError(f"{path.name} is missing {suffix.lstrip('/')}")

    forbidden = ("/rs13sols/", "/problemdata/", ".sol", ".problem.data")
    for name in names:
        normalized = f"/{name}"
        if any(token in normalized for token in forbidden):
            raise AssertionError(f"{path.name} includes forbidden maintenance data: {name}")

    member = next(name for name in names if name.endswith("/references.json"))
    if path.suffix == ".whl":
        with ZipFile(path) as archive:
            catalog = json.loads(archive.read(member))
    else:
        with tarfile.open(path, "r:gz") as archive:
            catalog = json.load(archive.extractfile(member))
    if catalog["schema"] != "rs13-best-known/2" or len(catalog["records"]) != 350:
        raise AssertionError(f"{path.name}: unexpected reference catalog")
    for entry in catalog["records"].values():
        if set(entry) != {"dimension", "problem_sha256", "bounds_sha256", "solution_sha256", "reference"}:
            raise AssertionError(f"{path.name}: unexpected reference data")
        if set(entry["reference"]) != {"fun", "maxcv", "kind", "source"}:
            raise AssertionError(f"{path.name}: reference must contain raw values/provenance, not points")


def main() -> None:
    dist = Path("dist")
    archives = [*dist.glob("*.whl"), *dist.glob("*.tar.gz")]
    if len(archives) != 2:
        raise RuntimeError(f"Expected one wheel and one sdist in {dist}, found {archives}")
    for archive in archives:
        _check_archive(archive)
        print(f"Checked {archive}")


if __name__ == "__main__":
    main()
