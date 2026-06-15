"""Extended analysis: sensitivity, TVC gap, OALA scenarios."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from mpf_simulator import (
    Participant,
    SimulationConfig,
    load_participants,
    result_to_dict,
    simulate_participant,
)

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output"


def baseline_comparison(cfg: SimulationConfig) -> pd.DataFrame:
    rows = [result_to_dict(simulate_participant(p, cfg)) for p in load_participants()]
    return pd.DataFrame(rows)


def fund_swap_sensitivity(cfg: SimulationConfig) -> pd.DataFrame:
    participants = load_participants()
    rows = []
    for p in participants:
        base = simulate_participant(p, cfg)
        swapped = simulate_participant(p, cfg, fund_override="global" if p.fund == "hong_kong" else "hong_kong")
        rows.append(
            {
                "name": p.name,
                "assigned_fund": p.fund,
                "balance_assigned": round(base.final_balance, 0),
                "balance_swapped": round(swapped.final_balance, 0),
                "rr_assigned_pct": round(base.replacement_ratio * 100, 1),
                "rr_swapped_pct": round(swapped.replacement_ratio * 100, 1),
                "fund_effect": round(swapped.final_balance - base.final_balance, 0),
            }
        )
    return pd.DataFrame(rows)


def start_age_sensitivity(cfg: SimulationConfig, ages: list[int] | None = None) -> pd.DataFrame:
    ages = ages or [20, 30, 40, 50]
    rows = []
    for age in ages:
        for fund in ["global", "hong_kong"]:
            p = Participant(name=f"Age{age}", start_age=age, fund=fund)
            r = simulate_participant(p, cfg)
            rows.append(
                {
                    "start_age": age,
                    "fund": fund,
                    "contribution_years": round(r.contribution_years, 1),
                    "final_balance": round(r.final_balance, 0),
                    "replacement_ratio_pct": round(r.replacement_ratio * 100, 1),
                }
            )
    return pd.DataFrame(rows)


def solve_extra_contribution(
    participant: Participant,
    cfg: SimulationConfig,
    target_replacement_ratio: float,
    max_extra: float = 20000.0,
) -> dict:
    """Binary search monthly TVC needed to reach target replacement ratio."""

    def rr(extra: float) -> float:
        return simulate_participant(participant, cfg, extra_monthly_contribution=extra).replacement_ratio

    low, high = 0.0, max_extra
    if rr(high) < target_replacement_ratio:
        required = None
    else:
        for _ in range(40):
            mid = (low + high) / 2
            if rr(mid) >= target_replacement_ratio:
                high = mid
            else:
                low = mid
        required = high

    base = simulate_participant(participant, cfg)
    with_extra = simulate_participant(participant, cfg, extra_monthly_contribution=required or 0.0)
    return {
        "name": participant.name,
        "target_replacement_ratio_pct": target_replacement_ratio * 100,
        "current_replacement_ratio_pct": round(base.replacement_ratio * 100, 1),
        "required_extra_monthly_contribution": round(required, 0) if required is not None else None,
        "achievable": required is not None,
        "balance_with_extra": round(with_extra.final_balance, 0),
        "replacement_ratio_with_extra_pct": round(with_extra.replacement_ratio * 100, 1),
    }


def tvc_gap_analysis(cfg: SimulationConfig) -> pd.DataFrame:
    assumptions = json.loads((DATA_DIR / "assumptions.json").read_text())
    targets = assumptions["target_replacement_ratios"]
    rows = []
    for p in load_participants():
        for target in targets:
            rows.append(solve_extra_contribution(p, cfg, target))
    return pd.DataFrame(rows)


def retirement_income_breakdown(cfg: SimulationConfig) -> pd.DataFrame:
    assumptions = json.loads((DATA_DIR / "assumptions.json").read_text())
    oala = assumptions["oala_2025_26"]
    rows = []

    for p in load_participants():
        base = simulate_participant(p, cfg)
        mpf_monthly = base.annual_retirement_income / 12

        for scenario, oala_monthly in [
            ("no_oala", 0),
            ("oala_normal", oala["normal_monthly"]),
            ("oala_higher", oala["higher_monthly"]),
        ]:
            total_monthly = mpf_monthly + oala_monthly
            rows.append(
                {
                    "name": p.name,
                    "scenario": scenario,
                    "mpf_monthly": round(mpf_monthly, 0),
                    "oala_monthly": oala_monthly,
                    "total_monthly": round(total_monthly, 0),
                    "final_monthly_salary": round(base.final_annual_salary / 12, 0),
                    "combined_replacement_ratio_pct": round(
                        (total_monthly * 12) / base.final_annual_salary * 100, 1
                    ),
                }
            )
    return pd.DataFrame(rows)


def tvc_marginal_effect(cfg: SimulationConfig, extras: list[float] | None = None) -> pd.DataFrame:
    extras = extras or [0, 500, 1000, 1500, 2000, 3000, 5000]
    rows = []
    for p in load_participants():
        for extra in extras:
            r = simulate_participant(p, cfg, extra_monthly_contribution=extra)
            rows.append(
                {
                    "name": p.name,
                    "extra_monthly_contribution": extra,
                    "final_balance": round(r.final_balance, 0),
                    "replacement_ratio_pct": round(r.replacement_ratio * 100, 1),
                }
            )
    return pd.DataFrame(rows)


def run_all(cfg: SimulationConfig | None = None) -> dict[str, pd.DataFrame]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cfg = cfg or SimulationConfig.from_json(DATA_DIR / "assumptions.json")

    tables = {
        "baseline_comparison": baseline_comparison(cfg),
        "fund_swap_sensitivity": fund_swap_sensitivity(cfg),
        "start_age_sensitivity": start_age_sensitivity(cfg),
        "tvc_gap_analysis": tvc_gap_analysis(cfg),
        "retirement_income_breakdown": retirement_income_breakdown(cfg),
        "tvc_marginal_effect": tvc_marginal_effect(cfg),
    }

    for name, df in tables.items():
        df.to_csv(OUTPUT_DIR / f"{name}.csv", index=False)

    return tables
