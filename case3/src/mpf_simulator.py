"""Core MPF defined-contribution simulation for Peter and Mary."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


@dataclass
class SimulationConfig:
    start_date: str = "2000-12-01"
    retirement_age: int = 65
    initial_monthly_salary: float = 20000.0
    employee_contribution_rate: float = 0.05
    employer_contribution_rate: float = 0.05
    relevant_income_cap_monthly: float = 30000.0
    withdrawal_rate_annual: float = 0.04
    forward_return_annual: float = 0.04
    fund_expense_ratio_annual: float = 0.01

    @classmethod
    def from_json(cls, path: Path) -> "SimulationConfig":
        payload = json.loads(path.read_text())["simulation"]
        return cls(**payload)


@dataclass
class Participant:
    name: str
    start_age: int
    fund: str


@dataclass
class SimulationResult:
    name: str
    start_age: int
    fund: str
    retirement_date: pd.Timestamp
    final_balance: float
    total_contributions: float
    total_investment_gain: float
    final_annual_salary: float
    replacement_ratio: float
    annual_retirement_income: float
    contribution_years: float
    history: pd.DataFrame = field(repr=False)


def _load_monthly_returns(fund: str) -> pd.Series:
    path = DATA_DIR / f"{fund}_monthly_returns.csv"
    df = pd.read_csv(path, parse_dates=["date"])
    return df.set_index("date")["monthly_return"]


def _load_cpi() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "hk_cpi_monthly.csv", parse_dates=["date"])


def _monthly_contribution(salary: float, cfg: SimulationConfig) -> float:
    capped_salary = min(salary, cfg.relevant_income_cap_monthly)
    rate = cfg.employee_contribution_rate + cfg.employer_contribution_rate
    return capped_salary * rate


def simulate_participant(
    participant: Participant,
    cfg: SimulationConfig,
    extra_monthly_contribution: float = 0.0,
    fund_override: str | None = None,
) -> SimulationResult:
    fund = fund_override or participant.fund
    returns = _load_monthly_returns(fund)
    cpi = _load_cpi().set_index("date")

    start = pd.Timestamp(cfg.start_date)
    retire = pd.Timestamp(start.year + (cfg.retirement_age - participant.start_age), start.month, 1)
    months = pd.date_range(start, retire, freq="MS")

    balance = 0.0
    salary = cfg.initial_monthly_salary
    total_contrib = 0.0
    rows: list[dict] = []
    expense_monthly = (1 + cfg.fund_expense_ratio_annual) ** (1 / 12) - 1
    forward_monthly = (1 + cfg.forward_return_annual) ** (1 / 12) - 1

    for i, dt in enumerate(months):
        age = participant.start_age + i / 12.0

        if i > 0 and dt in cpi.index:
            prev = months[i - 1]
            if prev in cpi.index and dt in cpi.index:
                salary *= cpi.loc[dt, "cpi_index"] / cpi.loc[prev, "cpi_index"]

        if dt in returns.index:
            gross_return = returns.loc[dt]
            return_source = "historical"
        else:
            gross_return = forward_monthly
            return_source = "projected"

        net_return = (1 + gross_return) * (1 - expense_monthly) - 1
        contrib = _monthly_contribution(salary, cfg) + extra_monthly_contribution
        balance = balance * (1 + net_return) + contrib
        total_contrib += contrib

        rows.append(
            {
                "date": dt,
                "age": age,
                "salary_monthly": salary,
                "contribution": contrib,
                "monthly_return": net_return,
                "return_source": return_source,
                "balance": balance,
            }
        )

    history = pd.DataFrame(rows)
    final_annual_salary = history.iloc[-12:]["salary_monthly"].mean() * 12
    annual_income = balance * cfg.withdrawal_rate_annual
    replacement_ratio = annual_income / final_annual_salary if final_annual_salary else 0.0

    return SimulationResult(
        name=participant.name,
        start_age=participant.start_age,
        fund=fund,
        retirement_date=retire,
        final_balance=balance,
        total_contributions=total_contrib,
        total_investment_gain=balance - total_contrib,
        final_annual_salary=final_annual_salary,
        replacement_ratio=replacement_ratio,
        annual_retirement_income=annual_income,
        contribution_years=len(months) / 12.0,
        history=history,
    )


def load_participants() -> list[Participant]:
    payload = json.loads((DATA_DIR / "assumptions.json").read_text())["participants"]
    return [
        Participant(name="Peter", start_age=payload["peter"]["start_age"], fund=payload["peter"]["fund"]),
        Participant(name="Mary", start_age=payload["mary"]["start_age"], fund=payload["mary"]["fund"]),
    ]


def result_to_dict(result: SimulationResult) -> dict:
    return {
        "name": result.name,
        "start_age": result.start_age,
        "fund": result.fund,
        "retirement_date": result.retirement_date.strftime("%Y-%m"),
        "contribution_years": round(result.contribution_years, 1),
        "total_contributions": round(result.total_contributions, 0),
        "final_balance": round(result.final_balance, 0),
        "total_investment_gain": round(result.total_investment_gain, 0),
        "final_annual_salary": round(result.final_annual_salary, 0),
        "annual_retirement_income": round(result.annual_retirement_income, 0),
        "monthly_retirement_income": round(result.annual_retirement_income / 12, 0),
        "replacement_ratio": round(result.replacement_ratio, 4),
        "replacement_ratio_pct": round(result.replacement_ratio * 100, 1),
    }
