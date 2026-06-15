"""Fetch market data for Case III MPF simulation."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

# Hong Kong Composite CPI year-on-year % change (C&SD, approximate annual figures)
HK_CPI_ANNUAL = {
    2000: 2.8,
    2001: -1.6,
    2002: -3.0,
    2003: -2.6,
    2004: -0.4,
    2005: 1.1,
    2006: 2.0,
    2007: 2.5,
    2008: 4.3,
    2009: 0.5,
    2010: 2.4,
    2011: 5.3,
    2012: 4.3,
    2013: 4.3,
    2014: 4.4,
    2015: 3.0,
    2016: 2.4,
    2017: 1.5,
    2018: 2.4,
    2019: 2.9,
    2020: 0.3,
    2021: 1.6,
    2022: 1.9,
    2023: 2.1,
    2024: 1.7,
    2025: 2.0,
    2026: 2.0,
    2027: 2.0,
    2028: 2.0,
    2029: 2.0,
    2030: 2.0,
    2031: 2.0,
    2032: 2.0,
    2033: 2.0,
    2034: 2.0,
    2035: 2.0,
    2036: 2.0,
    2037: 2.0,
    2038: 2.0,
    2039: 2.0,
    2040: 2.0,
    2041: 2.0,
    2042: 2.0,
    2043: 2.0,
    2044: 2.0,
    2045: 2.0,
}

# Global fund splice weights (developed US + developed ex-US before ACWI existed)
GLOBAL_US_WEIGHT = 0.65
GLOBAL_EFA_WEIGHT = 0.35
GLOBAL_BLEND_START = pd.Timestamp("2001-09-01")
GLOBAL_ACWI_START = pd.Timestamp("2008-04-01")
SIM_START = pd.Timestamp("2000-12-01")


def build_cpi_series(start: str = "2000-12-01", end: str = "2045-12-01") -> pd.DataFrame:
    """Build monthly CPI index from annual YoY inflation rates."""
    months = pd.date_range(start=start, end=end, freq="MS")
    index = 100.0
    records: list[dict] = []

    for dt in months:
        year = dt.year
        prev_year = year - 1
        annual_rate = HK_CPI_ANNUAL.get(prev_year, 2.0) / 100.0
        monthly_rate = (1 + annual_rate) ** (1 / 12) - 1
        if records:
            index *= 1 + monthly_rate
        records.append(
            {
                "date": dt,
                "cpi_index": index,
                "monthly_inflation": monthly_rate,
            }
        )

    df = pd.DataFrame(records)
    df.to_csv(DATA_DIR / "hk_cpi_monthly.csv", index=False)
    return df


def _download_close(ticker: str, start: str, end: str) -> pd.Series:
    data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=True)
    if data.empty:
        raise RuntimeError(f"No data returned for {ticker}")
    if isinstance(data.columns, pd.MultiIndex):
        return data["Close"].iloc[:, 0].dropna()
    return data["Close"].dropna()


def _monthly_returns(price: pd.Series) -> pd.Series:
    monthly = price.resample("MS").last().dropna()
    return monthly.pct_change().dropna()


def build_hong_kong_returns(end: str = "2046-01-01") -> pd.DataFrame:
    """Hong Kong Fund proxy: Hang Seng Index (^HSI).

    Tracker Fund (2800.HK) referenced in the case replicates the Hang Seng Index.
    ^HSI has complete daily history from MPF launch, avoiding Yahoo gaps for 2800.HK.
    """
    price = _download_close("^HSI", start="2000-11-01", end=end)
    returns = _monthly_returns(price)
    returns = returns[returns.index >= SIM_START]
    out = pd.DataFrame({"date": returns.index, "monthly_return": returns.values, "fund": "hong_kong"})
    out.to_csv(DATA_DIR / "hong_kong_monthly_returns.csv", index=False)
    return out


def build_global_returns(end: str = "2046-01-01") -> pd.DataFrame:
    """Global Fund proxy: spliced market indices with full history from Dec 2000.

    - Dec 2000 -- Aug 2001: S&P 500 (^GSPC), US developed market proxy
    - Sep 2001 -- Mar 2008: 65% ^GSPC + 35% EFA (developed ex-US)
    - Apr 2008 -- present: ACWI (broad global equity ETF)
    """
    gspc = _monthly_returns(_download_close("^GSPC", start="2000-11-01", end=end))
    efa = _monthly_returns(_download_close("EFA", start="2000-11-01", end=end))
    acwi = _monthly_returns(_download_close("ACWI", start="2008-01-01", end=end))

    months = pd.date_range(SIM_START, pd.Timestamp(end) - pd.offsets.MonthBegin(1), freq="MS")
    records: list[dict] = []

    for dt in months:
        if dt >= GLOBAL_ACWI_START and dt in acwi.index:
            ret = float(acwi.loc[dt])
            source = "ACWI"
        elif dt >= GLOBAL_BLEND_START and dt in gspc.index and dt in efa.index:
            ret = GLOBAL_US_WEIGHT * float(gspc.loc[dt]) + GLOBAL_EFA_WEIGHT * float(efa.loc[dt])
            source = "GSPC+EFA"
        elif dt in gspc.index:
            ret = float(gspc.loc[dt])
            source = "GSPC"
        else:
            continue
        records.append({"date": dt, "monthly_return": ret, "fund": "global", "source": source})

    out = pd.DataFrame(records)
    out.to_csv(DATA_DIR / "global_monthly_returns.csv", index=False)
    return out


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cpi = build_cpi_series()
    hk = build_hong_kong_returns()
    global_fund = build_global_returns()

    summary = {
        "cpi_months": len(cpi),
        "hong_kong_months": len(hk),
        "global_months": len(global_fund),
        "hong_kong_proxy": "^HSI (Hang Seng Index)",
        "hong_kong_rationale": "Tracker Fund 2800.HK replicates HSI; complete history from Dec 2000",
        "global_proxy": "Spliced: ^GSPC -> 65%^GSPC+35%EFA -> ACWI",
        "global_splice": {
            "2000-12_to_2001-08": "^GSPC",
            "2001-09_to_2008-03": "65% ^GSPC + 35% EFA",
            "2008-04_onwards": "ACWI",
        },
        "cpi_source": "C&SD Composite CPI YoY (annual), converted to monthly",
        "historical_coverage": "Dec 2000 to latest available market data",
    }
    (DATA_DIR / "data_summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
