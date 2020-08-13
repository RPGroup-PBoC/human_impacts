pdf: 
	pandoc styles/metadata.yml \
	$1/*.md\
	-o $1/$2.pdf \
	--filter=pandoc-crossref \
	--bibliography=$1/library.bib \
	--csl=cell.csl \


word:	
	pandoc metadata.yml \
	*.md \
	-o $1/$2.docx \
	--reference-doc=styles/template.docx \
	-f markdown+smart \
	--filter=pandoc-crossref \
	--bibliography=$1/library.bib \
	--csl=cell.csl 