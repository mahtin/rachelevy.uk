#
# Makefile for website testing locally - not used for github actions/workflows
#

SITEURL=http://localhost:8000
CONTENT=content
PELICAN=pelican
PELICANCONF=pelicanconf.py

all: output

output: .FORCE
	$(PELICAN) $(CONTENT) -o output -s $(PELICANCONF) -e 'SITEURL="$(SITEURL)"'
	@echo 'URLs in sitemap:' `fgrep '<loc>' < output/sitemap.xml | wc -l`

clean:
	rm -r output/*

.FORCE:
