# Modelling Assumptions — Case III

## Simulation Parameters

| Parameter | Value | Source / Note |
|-----------|-------|---------------|
| MPF launch / start date | 1 Dec 2000 | Case III |
| Retirement age | 65 | Case III |
| Initial monthly salary | HK$20,000 | Case III |
| Employee contribution | 5% | MPF mandatory |
| Employer contribution | 5% | MPF mandatory |
| Monthly total contribution (initial) | HK$2,000 | Case III |
| Relevant income cap | HK$30,000/month | MPF rules |
| Salary growth | HK Composite CPI | C&SD annual YoY |
| Hong Kong Fund proxy | **Hang Seng Index `^HSI`** | Tracker Fund (2800.HK) replicates HSI |
| Global Fund proxy | **Spliced indices** | See below |
| Historical period | Dec 2000 – latest available | Actual monthly returns |
| Forward period | After last available return | 4% p.a. assumed |
| Fund expense ratio | 1% p.a. | MPFA typical range |
| Retirement income method | 4% safe withdrawal rate | Standard pension planning |
| TVC tax deduction cap | HK$60,000/year | MPF TVC rules |

## Fund Return Proxies (Dec 2000 onwards)

### Hong Kong Fund (Mary)

- **Proxy:** Hang Seng Index (`^HSI`)
- **Rationale:** Case III assigns a Hong Kong Fund; the Tracker Fund (`2800.HK`) cited in the case study replicates the Hang Seng Index. `^HSI` provides complete historical data from MPF launch.

### Global Fund (Peter)

- **Proxy:** Spliced market indices (no single global ETF existed throughout 2000–2008)
  - Dec 2000 – Aug 2001: S&P 500 (`^GSPC`)
  - Sep 2001 – Mar 2008: 65% `^GSPC` + 35% `EFA` (MSCI EAFE)
  - Apr 2008 – present: `ACWI` (MSCI ACWI ETF)

## OALA Parameters (2025/26)

| Item | Amount (HK$) |
|------|----------------|
| Normal OALA (monthly) | 2,065 |
| Higher OALA (monthly) | 4,185 |
| Old Age Allowance (70+, monthly) | 1,500 |
| Asset limit (single, Higher OALA) | 401,000 |
| Income limit (single, Higher OALA) | 10,700/month |

Source: Social Welfare Department, Old Age Living Allowance scheme.

## Simplifications

1. Contributions occur at the beginning of each month.
2. Both employees remain continuously employed until age 65.
3. MPF mandatory cap history is not modelled year-by-year; current HK$30,000 cap applied throughout.
4. TVC gap analysis assumes extra contributions are invested in the same fund as mandatory contributions.
5. Peter and Mary retire in different calendar years (2045 and 2025 respectively) but both at age 65.
6. Post-2025 returns for Peter use a 4% forward assumption until retirement in 2045.
