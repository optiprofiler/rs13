#!/usr/bin/env python3
"""Inspect an RS13 runtime archive without adopting it."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "UPSTREAM_SNAPSHOT.json"
VENDORED_DIR = ROOT / "runtime" / "rs13pm"


def _defines_x0(source: str) -> bool:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        for target in targets:
            if isinstance(target, ast.Name) and target.id == "x0":
                return True
    return False


def inspect_archive(archive_path: Path) -> dict[str, object]:
    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    expected = snapshot["runtime"]
    expected_names = {path.name for path in VENDORED_DIR.glob("*.py")}

    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    archive_names: set[str] = set()
    files_with_x0 = 0
    with ZipFile(archive_path) as archive:
        for name in archive.namelist():
            path = Path(name)
            if path.suffix != ".py" or path.name == "__init__.py" or "__MACOSX" in path.parts:
                continue
            source = archive.read(name).decode("utf-8")
            archive_names.add(path.name)
            files_with_x0 += int(_defines_x0(source))

    missing = sorted(expected_names - archive_names)
    added = sorted(archive_names - expected_names)
    changed = digest != expected["sha256"]
    compatible = (
        not missing
        and not added
        and len(archive_names) == expected["python_problem_files"]
        and files_with_x0 == expected["files_with_x0"]
    )
    return {
        "pinned_sha256": expected["sha256"],
        "candidate_sha256": digest,
        "changed": changed,
        "candidate_problem_files": len(archive_names),
        "candidate_files_with_x0": files_with_x0,
        "missing_files": missing,
        "added_files": added,
        "adapter_contract_compatible": compatible,
        "decision": "review-required" if changed else "matches-pinned",
    }


def _write_markdown(result: dict[str, object], destination: Path) -> None:
    lines = [
        "# RS13 upstream runtime report",
        "",
        f"- Pinned archive SHA-256: `{result['pinned_sha256']}`",
        f"- Candidate archive SHA-256: `{result['candidate_sha256']}`",
        f"- Candidate Python problem files: {result['candidate_problem_files']}",
        f"- Candidate files defining `x0`: {result['candidate_files_with_x0']}",
        f"- Adapter contract compatible: `{str(result['adapter_contract_compatible']).lower()}`",
        "",
    ]
    if result["changed"]:
        lines.append("The official archive changed. It has not been adopted.")
    else:
        lines.append("The official archive matches the pinned runtime snapshot.")
    if result["missing_files"]:
        lines.append(f"Missing files: {', '.join(result['missing_files'][:20])}")
    if result["added_files"]:
        lines.append(f"Added files: {', '.join(result['added_files'][:20])}")
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    result = inspect_archive(args.archive)
    args.json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    _write_markdown(result, args.markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
