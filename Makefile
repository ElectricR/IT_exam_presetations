all: src/EGE_informatics_presentation_26.tex
	lualatex --shell-escape src/EGE_informatics_presentation_26.tex

c: 
	rm *.out *.toc *.snm *.pdf *.log *.aux *.nav *.vrb

o:
	xdg-open EGE_informatics_presentation_26.pdf

.PHONY: all c o
