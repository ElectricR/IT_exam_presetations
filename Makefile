all: src/EGE_informatics_presentation_26.tex
	lualatex src/EGE_informatics_presentation_26.tex

c: 
	rm *.out *.toc *.snm *.pdf *.log *.aux *.nav *.vrb

o:
	xdg-open EGE_informatics_presentation_26.pdf

.PHONY: all c o
