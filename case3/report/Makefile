.PHONY: all clean

MAIN = main.tex
PDF = main.pdf

all: $(PDF)

$(PDF): $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN)

clean:
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk
