"""Generate report figures for Case III."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from analysis import run_all
from mpf_simulator import SimulationConfig, load_participants, simulate_participant

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output"

plt.style.use("seaborn-v0_8-whitegrid")


def _save(fig: plt.Figure, name: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_balance_over_age(cfg: SimulationConfig) -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    for p in load_participants():
        result = simulate_participant(p, cfg)
        ax.plot(result.history["age"], result.history["balance"] / 1e6, label=p.name, linewidth=2)
    ax.set_xlabel("Age")
    ax.set_ylabel("MPF Balance (HK$ millions)")
    ax.set_title("MPF Balance Accumulation: Peter vs Mary")
    ax.legend()
    _save(fig, "fig1_balance_over_age.png")


def plot_income_breakdown(tables: dict[str, pd.DataFrame]) -> None:
    df = tables["retirement_income_breakdown"]
    focus = df[df["scenario"] == "integrated"].copy()
    labels = focus["name"].tolist()
    mpf = focus["mpf_monthly"].tolist()
    oala = focus["oala_monthly"].tolist()
    x = range(len(labels))
    width = 0.5

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x, mpf, width, label="MPF (4% withdrawal)", color="#1f77b4")
    ax.bar(x, oala, width, bottom=mpf, label="OALA", color="#ff7f0e")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel("Monthly Income (HK$)")
    ax.set_xlabel("Member")
    ax.set_title("Retirement Income: MPF plus OALA (Part c)")
    ax.legend()
    _save(fig, "fig2_income_breakdown.png")


def plot_start_age_sensitivity(tables: dict[str, pd.DataFrame]) -> None:
    df = tables["start_age_sensitivity"]
    fig, ax = plt.subplots(figsize=(9, 5))
    for fund, color in [("global", "#1f77b4"), ("hong_kong", "#ff7f0e")]:
        sub = df[df["fund"] == fund]
        ax.plot(sub["start_age"], sub["replacement_ratio_pct"], marker="o", label=fund.replace("_", " ").title())
    ax.set_xlabel("Contribution Start Age")
    ax.set_ylabel("Replacement Ratio (%)")
    ax.set_title("Effect of Start Age on Replacement Ratio")
    ax.legend()
    _save(fig, "fig3_start_age_sensitivity.png")


def plot_tvc_marginal_effect(tables: dict[str, pd.DataFrame]) -> None:
    df = tables["tvc_marginal_effect"]
    fig, ax = plt.subplots(figsize=(9, 5))
    for name in df["name"].unique():
        sub = df[df["name"] == name]
        ax.plot(sub["extra_monthly_contribution"], sub["replacement_ratio_pct"], marker="o", label=name)
    ax.axhline(60, color="gray", linestyle="--", linewidth=1, label="60% target")
    ax.axhline(70, color="gray", linestyle=":", linewidth=1, label="70% target")
    ax.set_xlabel("Extra Monthly Contribution (HK$)")
    ax.set_ylabel("Replacement Ratio (%)")
    ax.set_title("TVC Marginal Effect on Replacement Ratio")
    ax.legend()
    _save(fig, "fig4_tvc_marginal_effect.png")


def generate_all(cfg: SimulationConfig | None = None) -> dict[str, pd.DataFrame]:
    cfg = cfg or SimulationConfig.from_json(DATA_DIR / "assumptions.json")
    tables = run_all(cfg)
    plot_balance_over_age(cfg)
    plot_income_breakdown(tables)
    plot_start_age_sensitivity(tables)
    plot_tvc_marginal_effect(tables)
    return tables
