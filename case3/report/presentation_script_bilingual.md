# Case III Presentation Script — 中英文对照
## Defined Contribution Plan & MPF | 界定供款计划与强积金

**Course 课程:** AMA1D03 Introduction to Pension Mathematics  
**Duration 时长:** about 4 minutes 约 4 分钟  
**Tip 提示:** Show `fig1_balance_over_age.png` during Section 2, and `fig4_tvc_marginal_effect.png` during Section 3.

---

## [0:00–0:30] Opening 开场

**EN:**  
Good morning/afternoon. Our presentation is Case III: Defined Contribution Plan and MPF retirement planning. We compare two employees, Peter and Mary, to answer one key question: **Is mandatory MPF enough for retirement, and should they add extra contributions?**

**中文:**  
大家好。我们汇报的是 Case III：界定供款计划与强积金退休规划。我们通过 Peter 和 Mary 两个案例，回答一个核心问题：**仅靠强制强积金是否足够退休？是否需要额外供款？**

---

## [0:30–1:15] (a) MPF System Overview 制度简介

**EN:**  
Hong Kong's MPF, launched in December 2000, is a compulsory **defined contribution** scheme. Both employee and employer contribute 5% each. The final benefit depends on contributions, investment returns, and fees — not a guaranteed pension.

MPF is the **second pillar** of Hong Kong's retirement system, together with government allowances like OALA (first pillar) and personal savings (third pillar).

**中文:**  
香港强积金自 2000 年 12 月推出，是强制性**界定供款**计划。雇员和雇主各供款 5%。退休金额取决于供款、投资回报和费用，而不是预先保证的养老金。

强积金属于香港退休体系的**第二支柱**，第一支柱是政府津贴（如长者生活津贴 OALA），第三支柱是个人储蓄。

---

## [1:15–2:45] (b) Peter vs Mary — Key Results 核心结果

**EN:**  
Peter starts contributing at age 20 in a **Global Fund**. Mary starts at age 40 in a **Hong Kong Fund**. Both earn HK$20,000 per month initially, retire at 65, and each contributes HK$2,000 per month including employer matching.

Using a Python simulation with historical market data from December 2000:

| | Peter | Mary |
|---|-------|------|
| Contribution years | 45 years | 25 years |
| Final MPF balance | **HK$5.0 million** | **HK$0.85 million** |
| Replacement ratio | **36%** | **9.1%** |

**中文:**  
Peter 从 20 岁开始投资**全球基金**，Mary 从 40 岁开始投资**香港基金**。两人初始月薪都是 2 万港元，65 岁退休，每月总供款（含雇主配对）都是 2,000 港元。

我们用 Python 模拟了自 2000 年 12 月以来的真实市场数据，结果是：

| | Peter | Mary |
|---|-------|------|
| 供款年数 | 45 年 | 25 年 |
| 退休强积金余额 | **约 500 万港元** | **约 85 万港元** |
| 替代率 | **36%** | **9.1%** |

---

**EN:**  
Financial planners often target a **60% replacement ratio**. Peter reaches only 36%; Mary only 9.1%. Both are far below the target.

Our sensitivity analysis shows: **starting age matters more than fund choice.** Even if Mary switches to a global fund, her ratio rises to only about 22% — still much lower than Peter's 36%.

**中文:**  
财务规划通常以 **60% 替代率** 为目标。Peter 只有 36%，Mary 只有 9.1%，都远低于目标。

敏感性分析显示：**开始供款的年龄比选哪只基金更重要。** 即使 Mary 改投全球基金，替代率也只有约 22%，仍远低于 Peter 的 36%。

---

**EN:**  
Why is the gap so large? Because Peter has **20 more years** of contributions and compounding. In a DC system, time in the market is the most powerful factor.

**中文:**  
为什么差距这么大？因为 Peter 多了 **20 年** 供款和复利时间。在 DC 制度下，供款时间是最关键的变量。

---

## [2:45–3:45] (c) Social Security & Recommendations 社会保障与建议

**EN:**  
Hong Kong has no universal earnings-related public pension. OALA provides HK$2,065 to HK$4,185 per month, but members with large MPF balances may not qualify.

For Mary, even MPF plus Higher OALA gives only about **22.5%** replacement — still insufficient.

**Should they add extra contributions (TVC)?**
- **Peter:** Yes, moderately — about **HK$1,600 per month** to reach 60%.
- **Mary:** Yes, urgently — but TVC alone is not realistic. She needs OALA, delayed retirement, and third-pillar savings.

**中文:**  
香港没有全民、与收入挂钩的公共养老金。OALA 每月约 2,065 至 4,185 港元，但强积金余额较高者可能不符合资格。

对 Mary 来说，即使强积金加上高额 OALA，综合替代率也只有约 **22.5%**，仍然不够。

**两人是否应该增加额外供款（TVC）？**
- **Peter：应该，但量不大** — 每月约 **1,600 港元** 可达 60% 替代率。
- **Mary：非常需要，但单靠 TVC 不现实** — 还要结合 OALA、延迟退休和第三支柱储蓄。

---

## [3:45–4:15] Conclusion 结论

**EN:**  
To summarize: mandatory MPF alone is **not enough** for either Peter or Mary. Early and consistent contributions are essential. Social security helps lower-asset retirees but cannot replace inadequate lifetime savings. **Both should make extra contributions — Mary needs it far more urgently.**

Thank you.

**中文:**  
总结：对 Peter 和 Mary 来说，**强制强积金都不够**。尽早、持续供款至关重要。社会保障只能帮助低资产长者，无法替代不足的终身储蓄。**两人都应增加额外供款，其中 Mary 的紧迫性远高于 Peter。**

谢谢。

---

## Quick Reference Card 速记卡

| Point 要点 | EN | 中文 |
|------------|----|------|
| Peter RR | 36% | 36% |
| Mary RR | 9.1% | 9.1% |
| Peter TVC for 60% | ~HK$1,600/mo | 约 1,600 港元/月 |
| Main lesson | Start early > pick fund | 早供款 > 选基金 |
| Answer | Both need TVC; Mary urgent | 两人都要 TVC；Mary 更急 |

---

## Timing Guide 时间分配

| Section | Time |
|---------|------|
| Opening | 30 sec |
| (a) MPF overview | 45 sec |
| (b) Peter vs Mary | 90 sec |
| (c) OALA & TVC | 60 sec |
| Conclusion | 30 sec |
| **Total** | **~4 min** |

*To stretch to 5 minutes: pause on the comparison table and explain Figure 1.  
To shorten to 3 minutes: skip the sensitivity sentence and compress section (a).*
