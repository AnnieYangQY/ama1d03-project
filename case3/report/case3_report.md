# Section II — Case III: Defined Contribution Plan (MPF)

**Course:** AMA1D03 Introduction to Pension Mathematics  
**Topic:** Mandatory Provident Fund and Defined Contribution Retirement Planning

---

## (a) Descriptions of the Defined Contribution Plan and Its Application in the Pension System

### 1. Defined Contribution (DC) vs Defined Benefit (DB)

Under a **defined contribution (DC)** plan, the retirement benefit is not predetermined. Instead, the employer and/or employee contribute a specified amount into an individual account. The final benefit depends on:

- Total contributions made over the working life
- Investment returns earned on those contributions
- Fees deducted by fund managers

Investment and longevity risks are borne primarily by the member. By contrast, a **defined benefit (DB)** plan promises a benefit formula (e.g., a percentage of final salary × years of service), with the sponsor bearing most investment and longevity risk.

Hong Kong's Mandatory Provident Fund (MPF) System, launched on **1 December 2000**, is a compulsory DC scheme and forms the **second pillar** of Hong Kong's retirement protection framework, supplementing:

- **First pillar:** Non-contributory social assistance (e.g., Old Age Living Allowance, Old Age Allowance)
- **Third pillar:** Personal savings, insurance, and family support

### 2. Types of MPF Schemes

MPF schemes are classified into three main types (MPFA):

| Scheme Type | Description |
|-------------|-------------|
| Master Trust Schemes | Open to employees of participating employers and self-employed persons |
| Employer-sponsored Schemes | Only for employees of a single employer |
| Industry Schemes | For employees in specific industries (e.g., catering, construction) |

Each employee has a **personal account** within a scheme. When changing jobs, accrued benefits are portable and can be transferred to the new employer's scheme or a personal account.

### 3. Mandatory and Voluntary Contributions

**Mandatory Contributions (MC):**

- Both employee and employer each contribute **5%** of the employee's *relevant income*
- Relevant income is subject to minimum (HK$7,100) and maximum (HK$30,000) monthly thresholds
- Maximum mandatory contribution per party: HK$1,500/month

**Voluntary Contributions:**

- **Voluntary contributions (VC)** within an MPF scheme — set by employer or employee
- **Tax Deductible Voluntary Contributions (TVC)** — personal contributions up to **HK$60,000 per year** deductible for salaries tax

In the Case III example, Peter and Mary each contribute HK$1,000 (5% of HK$20,000 salary), matched equally by their employers, giving a total monthly contribution of **HK$2,000**.

### 4. Benefits, Withdrawal, and Retirement Age

Members can generally withdraw accrued benefits when reaching age **65** (the normal retirement age). Other early withdrawal conditions include:

- Permanent departure from Hong Kong
- Total incapacity
- Terminal illness
- Early retirement at age 60 with cessation of employment

Upon withdrawal, members may take a **lump sum** or convert part of the balance into an **annuity** through the MPF platform, providing a stream of retirement income.

### 5. Investment Options, Returns, and Fees

MPF offers multiple fund types:

- Equity (Hong Kong, China, Asia, Global)
- Mixed assets
- Bond and guaranteed funds
- Money market and index-tracking funds (e.g., Tracker Fund of Hong Kong)

Members bear **investment risk**. Historical returns vary significantly across fund types and periods. Fund managers charge **management fees** (typically 0.5%–2% per annum) and other expenses, which reduce net returns over long horizons.

In Case III, Peter invests in a **Global Fund** while Mary invests in a **Hong Kong Fund**, illustrating how asset allocation affects long-term outcomes under the same contribution structure.

### 6. Tax Treatment

Mandatory MPF contributions are tax-exempt up to the statutory limits. TVC provides an additional tax incentive for members seeking to close retirement income gaps. This is particularly relevant when mandatory contributions alone produce a low **replacement ratio**.

### 7. Role in Hong Kong's Pension System

MPF is designed to provide a basic level of retirement savings for the working population. However, academic and industry studies consistently show that mandatory contributions alone are **insufficient** to maintain pre-retirement living standards. Members are expected to supplement MPF with voluntary savings (TVC), other investments, and where eligible, government cash benefits.

---

## (b) Compare and Analyze the Defined Contribution Plan — Peter and Mary Examples

### 1. Modelling Setup

We simulate monthly MPF accumulation from December 2000 until each member reaches age 65:

| | Peter | Mary |
|---|-------|------|
| Start age (Dec 2000) | 20 | 40 |
| Retirement age | 65 | 65 |
| Contribution period | 45 years | 25 years |
| Retirement year | 2045 | 2025 |
| Assigned fund | Global (ACWI proxy) | Hong Kong (2800.HK proxy) |
| Initial monthly salary | HK$20,000 | HK$20,000 |
| Monthly MC (employee + employer) | HK$2,000 | HK$2,000 |

Salaries and contributions grow with the **Hong Kong Composite CPI**. Historical fund returns are used where available; a **4% annual return** is assumed thereafter. A **1% annual expense ratio** is deducted. Retirement income is estimated using the **4% safe withdrawal rule**.

Full assumptions are documented in `case3/data/assumptions.md`.

### 2. Baseline Results

| Indicator | Peter (Global) | Mary (Hong Kong) |
|-----------|----------------|------------------|
| Contribution years | 45.1 | 25.1 |
| Total contributions | HK$1,443,931 | HK$723,931 |
| Investment gains | HK$3,415,445 | HK$307,137 |
| Final MPF balance | **HK$4,859,376** | **HK$1,031,068** |
| Final annual salary | HK$555,156 | HK$374,107 |
| Annual retirement income (4%) | HK$194,375 | HK$41,243 |
| Monthly retirement income | HK$16,198 | HK$3,437 |
| **Replacement ratio** | **35.0%** | **11.0%** |

*Source: Python simulation (`case3/main.py`), output in `case3/output/baseline_comparison.csv`.*

**Figure 1** (`fig1_balance_over_age.png`) shows Peter's balance rising steeply over 45 years, while Mary's balance grows more slowly over 25 years, ending at roughly one-fifth of Peter's balance.

### 3. Advantages of the DC / MPF System

1. **Employer matching:** The employer's 5% contribution doubles the member's savings without additional employee cost.
2. **Portability:** Accrued benefits follow the employee across jobs.
3. **Investment choice:** Members can select funds aligned with risk tolerance and return objectives.
4. **Tax incentives:** TVC of up to HK$60,000/year is tax-deductible.
5. **Compounding over time:** Early starters like Peter benefit enormously from decades of compound growth — investment gains (HK$3.42M) far exceed contributions (HK$1.44M).

### 4. Disadvantages and Risks

1. **Investment risk:** Mary's Hong Kong fund underperformed the global fund over the sample period; members bear full downside risk.
2. **Low replacement ratio:** Even Peter achieves only 35% replacement from mandatory contributions — well below the 60–70% commonly recommended.
3. **Fee drag:** Management fees compound negatively over 25–45 years.
4. **No inflation guarantee:** While salaries adjust with CPI, retirement income depends on uncertain market returns.
5. **Late starter penalty:** Mary's 11% replacement ratio demonstrates that starting at 40 rather than 20 cannot be fully offset by fund selection.

### 5. Start Age vs Fund Choice — Which Matters More?

**Start-age sensitivity** (same HK$2,000 initial monthly contribution):

| Start Age | Global Fund RR | HK Fund RR |
|-----------|----------------|------------|
| 20 | 35.0% | 19.9% |
| 30 | 29.1% | 15.4% |
| 40 | 21.3% | 11.0% |
| 50 | 6.5% | 5.4% |

**Fund-swap sensitivity** (keeping the same start age):

| | Assigned Fund | Swapped Fund | RR Change |
|---|---------------|--------------|-----------|
| Peter (age 20) | Global: 35.0% | HK: 19.9% | −15.1 pp |
| Mary (age 40) | HK: 11.0% | Global: 21.3% | +10.3 pp |

**Key finding:** Peter at age 20 with the *underperforming* Hong Kong fund (19.9%) still achieves a higher replacement ratio than Mary at age 40 with the *better* global fund (21.3%) is close — but Peter's absolute balance (HK$4.86M vs Mary's HK$1.99M in swapped scenario) is far higher. More importantly, comparing start ages at the same fund shows a **24 percentage-point gap** (35% vs 11% for global), far exceeding the fund-selection effect for Mary (+10.3 pp). **Contribution horizon dominates fund selection.**

### 6. Living Expenses and Replacement Ratio

Financial planners often target a **60–70% replacement ratio** to maintain living standards in retirement (accounting for reduced work-related expenses).

| Member | MPF Monthly Income | Final Monthly Salary | Gap to 60% Target |
|--------|-------------------|---------------------|-------------------|
| Peter | HK$16,198 | HK$46,263 | HK$11,360/month |
| Mary | HK$3,437 | HK$31,176 | HK$15,269/month |

Mary faces a larger relative gap despite a lower final salary, confirming that late enrolment in a DC plan leaves members severely underfunded.

### 7. Inflation and Investment Return Effects

Salaries and mandatory contributions are indexed to CPI, so nominal balances grow with inflation. However:

- Real purchasing power of retirement income depends on whether investment returns exceed inflation
- Periods of low returns (e.g., post-2008, COVID-19 volatility) disproportionately affect members nearing retirement (Mary's case)
- A 1% fee differential over 45 years can reduce final balance by 10–15%

### 8. Should Peter and Mary Add Extra Contributions?

| Member | Current RR | Extra Monthly TVC for 60% RR | Extra Monthly TVC for 70% RR |
|--------|-----------|------------------------------|------------------------------|
| Peter | 35.0% | HK$1,703 | HK$2,384 |
| Mary | 11.0% | **HK$10,482** | **HK$12,623** |

**Figure 4** (`fig4_tvc_marginal_effect.png`) shows the marginal impact of additional monthly contributions on replacement ratio.

- **Mary** urgently needs substantial TVC or other income sources; mandatory MPF alone is inadequate.
- **Peter** benefits from early compounding but still requires ~HK$1,700/month extra to reach 60% RR — achievable within the TVC tax-deductible limit if planned annually.

---

## (c) Supporting Retirement Under DC with the Social Security System

### 1. Hong Kong Three-Pillar Framework

```
First Pillar (Government)     →  OALA, Old Age Allowance, CSSA
Second Pillar (Employer/MC)   →  MPF mandatory + voluntary (TVC)
Third Pillar (Personal)       →  Private savings, insurance, family
```

Unlike Canada's CPP or the US Social Security system, Hong Kong has **no universal earnings-related public pension**. Government support is means-tested and modest in amount.

### 2. Old Age Living Allowance (OALA)

Eligible Hong Kong residents aged 65+ may receive:

| Allowance | Monthly Amount (2025/26) |
|-----------|--------------------------|
| Normal OALA | HK$2,065 |
| Higher OALA | HK$4,185 |

Eligibility depends on income and asset tests. For a single person, the asset limit for Higher OALA is approximately **HK$401,000**. **MPF accrued benefits not yet withdrawn may be counted as assets**, potentially disqualifying members with substantial MPF balances from Higher OALA.

### 3. Combined Retirement Income — Peter's Example (Retirement 2045)

| Income Source | Monthly (HK$) | Notes |
|---------------|---------------|-------|
| MPF (4% withdrawal) | 16,198 | From HK$4.86M balance |
| OALA (Normal) | 2,065 | May fail asset test if MPF counted |
| OALA (Higher) | 4,185 | Unlikely if MPF balance counted as asset |
| **Combined (MPF + Normal OALA)** | **18,263** | Replacement ratio: 39.5% |
| Target (60% of final salary) | 27,758 | Gap: HK$9,495/month |

**Peter's strategy:**

1. Continue mandatory MPF until 65 — already on track for a solid base.
2. Add TVC of ~HK$1,700/month to reach 60% replacement ratio from MPF alone.
3. OALA may not be available given expected asset levels; plan should **not** rely on it.
4. Consider MPF **annuitisation** for longevity protection rather than full lump-sum withdrawal.
5. At age 70+, Old Age Allowance (HK$1,500/month) may supplement income with a separate eligibility test.

### 4. Combined Retirement Income — Mary's Example (Retirement 2025)

| Income Source | Monthly (HK$) | Notes |
|---------------|---------------|-------|
| MPF (4% withdrawal) | 3,437 | From HK$1.03M balance |
| OALA (Normal) | 2,065 | More likely eligible — lower assets |
| OALA (Higher) | 4,185 | Possible if assets below HK$401K |
| **Combined (MPF + Normal OALA)** | **5,502** | Replacement ratio: 17.6% |
| **Combined (MPF + Higher OALA)** | **7,622** | Replacement ratio: 24.4% |
| Target (60% of final salary) | 18,706 | Gap: HK$11,084/month (even with Higher OALA) |

**Figure 2** (`fig2_income_breakdown.png`) illustrates the income composition.

**Mary's strategy:**

1. **Strongly recommended:** Begin TVC immediately — ~HK$10,500/month needed for 60% RR from MPF alone (may be impractical; a mix of TVC, delayed retirement, and spending adjustment is needed).
2. Apply for **Higher OALA** if asset test permits (MPF balance at retirement may still exceed limit).
3. Consider **working beyond 65** to extend contribution period and delay drawdown.
4. Explore **MPF annuitisation** to guarantee minimum monthly income.
5. Build **third-pillar savings** (bank deposits, insurance) given limited time for compounding.

### 5. Illustrative Monthly Budget at Retirement

**Peter (age 65, 2045):**

| Item | Amount (HK$) |
|------|-------------|
| MPF income | 16,198 |
| TVC supplement (recommended) | 11,360 |
| **Total planned income** | **27,558** |
| Estimated essential expenses (60% of final salary) | 27,758 |

**Mary (age 65, 2025) — realistic mixed plan:**

| Item | Amount (HK$) |
|------|-------------|
| MPF income | 3,437 |
| Higher OALA | 4,185 |
| Part-time work / third-pillar savings | 5,000 |
| **Total planned income** | **12,622** |
| Essential expenses (60% of final salary) | 18,706 |
| **Remaining gap** | **6,084** |

Mary's case demonstrates a structural limitation of Hong Kong's DC system for late starters: even combining MPF, OALA, and modest additional income, reaching 60% replacement is challenging without significant lifestyle adjustment or extended working years.

### 6. Conclusions on Extra Contributions

| Question | Peter | Mary |
|----------|-------|------|
| Is mandatory MPF sufficient? | No (35% RR) | No (11% RR) |
| Should they add TVC? | **Yes** — moderate amount (~HK$1,700/month) | **Yes** — as much as affordable; ideally started earlier |
| Can social security fill the gap? | Unlikely (asset test) | Partially (OALA), but insufficient alone |
| Recommended approach | MPF + TVC + private savings | MPF + OALA + TVC + delayed retirement + third pillar |

Hong Kong's DC system effectively shifts retirement responsibility to the individual. Early, consistent contributions compounded over decades — as in Peter's case — are the most powerful lever. Social security (OALA) provides a safety net for lower-asset retirees but cannot substitute for inadequate lifetime savings. **Both Peter and Mary should make extra contributions; the urgency and required amount are far greater for Mary.**

---

## References

1. Mandatory Provident Fund Schemes Authority (MPFA). *MPF Fund Performance Platform.* https://mfp.mpfa.org.hk/
2. Social Welfare Department. *Old Age Living Allowance.* https://www.swd.gov.hk/oala/
3. Census and Statistics Department. *Composite Consumer Price Index.*
4. Hong Kong Mortgage Corporation. *MPF Related Information.*
5. Investopedia. *Individual Retirement Account (IRA).* https://www.investopedia.com/terms/i/ira.asp
6. Case III simulation outputs: `case3/output/`

## Appendix

- **Assumptions:** `case3/data/assumptions.md`
- **Python code:** `case3/src/` (run `python3 case3/main.py` to reproduce all tables and figures)
- **Figures:** `case3/output/fig1–fig4`
- **Data tables:** `case3/output/*.csv`
