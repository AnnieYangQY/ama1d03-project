"""Run full Case III data pipeline."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from fetch_data import main as fetch_main  # noqa: E402
from plots import generate_all  # noqa: E402


def main() -> None:
    print("Step 1: Fetching market and CPI data...")
    fetch_main()

    print("Step 2: Running simulation, analysis, and plots...")
    tables = generate_all()

    summary = {
        "baseline_comparison": tables["baseline_comparison"].to_dict(orient="records"),
        "tvc_gap_analysis": tables["tvc_gap_analysis"].to_dict(orient="records"),
        "fund_swap_sensitivity": tables["fund_swap_sensitivity"].to_dict(orient="records"),
    }
    out = ROOT / "output" / "summary.json"
    out.write_text(json.dumps(summary, indent=2))
    print(f"Done. Results written to {ROOT / 'output'}")


if __name__ == "__main__":
    main()
