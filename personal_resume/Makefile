all: 
	tex
	pdf
	clean	

tex:
	python ../generator.py -d resume.yml -p preferences.yml -o resume.tex

pdf:
	pdflatex -synctex=1 -interaction=nonstopmode resume.tex
	
clean:
	rm *.tex *.aux *.log *.run.xml *.bcf
