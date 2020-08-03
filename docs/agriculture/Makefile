pdf: 
	pandoc metadata.yml \
	*.md \
	-o agriculture.pdf \
	--filter=pandoc-crossref \
	--bibliography=library.bib \
	--csl=cell.csl 

word:	
	pandoc metadata.yml  -f markdown+smart --filter=pandoc-fignos --filter=pandoc-citeproc --bibliography=library.bib  -s *.md -o agriculture.docx