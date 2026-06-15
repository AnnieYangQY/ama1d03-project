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


def fetch_etf_returns(
    ticker: str,
    label: str,
    start: str = "2000-11-01",
    end: str = "2045-12-31",
) -> pd.DataFrame:
    """Download adjusted close prices and compute monthly returns."""
    data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=True)
    if data.empty:
        raise RuntimeError(f"No data returned for {ticker}")

    if isinstance(data.columns, pd.MultiIndex):
        price = data["Close"].iloc[:, 0]
    else:
        price = data["Close"]

    monthly = price.resample("MS").last().dropna()
    returns = monthly.pct_change().dropna()
    out = pd.DataFrame({"date": returns.index, "monthly_return": returns.values})
    out["fund"] = label
    out.to_csv(DATA_DIR / f"{label}_monthly_returns.csv", index=False)
    return out


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cpi = build_cpi_series()
    hk = fetch_etf_returns("2800.HK", "hong_kong")
    # URTH tracks MSCI World; available from 2012. Use ACWI for longer history.
    try:
        global_fund = fetch_etf_returns("ACWI", "global")
    except RuntimeError:
        global_fund = fetch_etf_returns("URTH", "global")

    summary = {
        "cpi_months": len(cpi),
        "hong_kong_months": len(hk),
        "global_months": len(global_fund),
        "hong_kong_ticker": "2800.HK",
        "global_ticker": "ACWI",
        "cpi_source": "C&SD Composite CPI YoY (annual), converted to monthly",
        "note": "ACWI used as Global Fund proxy; 2800.HK as Hong Kong Fund proxy.",
    }
    (DATA_DIR / "data_summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
