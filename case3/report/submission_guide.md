# Case III Submission Guide

## Completed Deliverables

| Item | Location | Status |
|------|----------|--------|
| Python pipeline | `case3/main.py` | Done |
| Simulation results | `case3/output/*.csv` | Done |
| Figures (4) | `case3/output/fig1–fig4.png` | Done |
| Assumptions doc | `case3/data/assumptions.md` | Done |
| Report draft (a)(b)(c) | `case3/report/case3_report.md` | Done |
| Video script | `case3/report/video_script.md` | Done |
| Cross-validation | `case3/src/validate.py` | Passed |

## Remaining Manual Steps

1. **Format report for submission**
   - Primary source: `case3/report/main.tex`
   - Compile: `cd case3/report && make`
   - Output PDF: `case3/report/main.pdf`
   - Font: Times New Roman 12pt; margins 1"; line spacing 1.0
   - Add your name/student ID on the title page if required
   - Ensure body is 6–12 pages (cover and appendix excluded)

2. **Record video (≤10 min)**
   - Follow `case3/report/video_script.md`
   - Show at least: baseline table, fig1, fig3, fig4

3. **Blackboard upload**
   - PDF report + video file
   - Due: 5 July 2026, 23:59

4. **Turnitin**
   - Submit report PDF through Turnitin before final Blackboard upload

## Fund Return Proxies (chosen scheme)

| Fund | Proxy | Rationale |
|------|-------|-----------|
| Hong Kong (Mary) | `^HSI` Hang Seng Index | Tracker Fund 2800.HK replicates HSI; full data from Dec 2000 |
| Global (Peter) | Spliced `^GSPC` → 65%`^GSPC`+35%`EFA` → `ACWI` | No single global ETF existed 2000–2008 |

Historical coverage: **307 monthly returns** from Dec 2000 to latest market data.

## Key Numbers (updated)

- Peter: HK$4.996M balance, 36.0% RR, needs HK$1,582/month TVC for 60%
- Mary: HK$0.851M balance, 9.1% RR, needs HK$13,205/month TVC for 60%
- Start age effect (20 vs 40, global): 36.0% vs 22.1% RR
