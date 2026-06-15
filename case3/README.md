# Case III — Defined Contribution Plan (MPF)

Python pipeline for AMA1D03 Section II Case III: Peter vs Mary MPF simulation.

## Quick Start

```bash
cd case3
pip install -r requirements.txt
python3 main.py
python3 src/validate.py
```

## Outputs

| Path | Description |
|------|-------------|
| `output/baseline_comparison.csv` | Peter vs Mary core results |
| `output/tvc_gap_analysis.csv` | TVC needed for 60%/70% RR |
| `output/fig1–fig4` | Report figures |
## Report (LaTeX)

**英文版：**
```bash
cd case3/report
make          # 输出 main.pdf
```

**中文版：**
```bash
cd case3/report
make zh       # 输出 main_zh.pdf（需 XeLaTeX）
```

| 文件 | 说明 |
|------|------|
| `main.tex` | 英文报告源文件 |
| `main_zh.tex` | 中文报告源文件 |
| `main.pdf` | 英文 PDF |
| `main_zh.pdf` | 中文 PDF |

格式：12pt、页边距 1 英寸、单倍行距；英文 Times New Roman，中文宋体。
| `report/video_script.md` | 10-minute presentation script |

## Reproduce

```bash
python3 main.py          # fetch data + simulate + plot
python3 src/validate.py  # cross-check key properties
```

## Structure

```
case3/
  data/           assumptions, CPI, fund returns
  src/            fetch_data, mpf_simulator, analysis, plots, validate
  output/         CSV tables and PNG figures
  report/         report draft and video script
  main.py         one-click pipeline
```
