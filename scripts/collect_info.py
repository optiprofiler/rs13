from pathlib import Path
import os
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rs13_tools import rs13_collect_info


REQUIRED_INPUTS = ("RS13PM_DIR", "RS13SOLS_DIR", "RS13_PROBLEMDATA_DIR")


def main():
    missing = [name for name in REQUIRED_INPUTS if not os.environ.get(name)]
    if missing:
        raise RuntimeError(
            "RS13 metadata regeneration requires all official inputs; missing "
            + ", ".join(missing)
        )
    rows = rs13_collect_info(refresh=True)
    statuses = {}
    for row in rows:
        status = row.get("problemdata_status", "")
        statuses[status] = statuses.get(status, 0) + 1
    print(f"Wrote {len(rows)} rows to {ROOT / 'probinfo_rs13.csv'}")
    print("problemdata_status:", statuses)


if __name__ == "__main__":
    main()
