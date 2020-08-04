pdf: 
	pandoc metadata.yml \
	*.md \
	-o agriculture.pdf \
	--filter=pandoc-crossref \
	--bibliography=library.bib \
	--csl=cell.csl \


word:	
	pandoc metadata.yml \
	*.md \
	-o agriculture.docx \
	--reference-doc=template.docx \
	-f markdown+smart \
	--filter=pandoc-crossref \
	--bibliography=library.bib \
	--csl=cell.csl 