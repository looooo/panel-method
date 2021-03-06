#!/usr/bin/bash
BASEDIR=$(dirname $0)
FILENAME=Gleitschirm_Potential_Strömung
OUTDIR=build/doc/

cd $BASEDIR
mkdir $OUTDIR -p

cd doc/latex_doc/tex
pdflatex $FILENAME.tex

bibtex $FILENAME
makeindex $FILENAME.nlo -s nomencl.ist -o $FILENAME.nls

pdflatex $FILENAME.tex
pdflatex $FILENAME.tex
rm *.aux *.ilg *.log *.toc *.nlo *.bbl *.blg # *.nls 
mv $FILENAME.pdf ../../../$OUTDIR

cd ../../..
cp doc/tutorial build/doc/ -r

# evince build/doc/$FILENAME.pdf &
