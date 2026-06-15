.PHONY: all zh clean

MAIN = main.tex
MAIN_ZH = main_zh.tex
PDF = main.pdf
PDF_ZH = main_zh.pdf

all: $(PDF)

zh: $(PDF_ZH)

$(PDF): $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN)

$(PDF_ZH): $(MAIN_ZH)
	xelatex -interaction=nonstopmode $(MAIN_ZH)
	xelatex -interaction=nonstopmode $(MAIN_ZH)

clean:
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk
