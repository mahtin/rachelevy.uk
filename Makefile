#
# Makefile for local website viewing/testing - not used for github actions/workflows
#

URL=rachellevy.uk

SITEURL=https://$(URL)/

CONTENT=content
PELICAN=pelican
PELICANCONF=pelicanconf.py

ENC_SITEURL=sc-domain:rachellevy.uk

GOOGLE_SEARCH_CONSOLE=https://www.googleapis.com/webmasters/v3/sites
SITEMAP=https%3A%2F%2F$(URL)%2Fsitemap.xml

# this will expire soon ...
GOOGLE_SEARCH_CONSOLE_ACCESS_TOKEN_FILE=~/.google_search_console_access_token

LOCAL_SITEURL=http://localhost:8000

all: CHANGELOG.md output

output: .FORCE
	$(PELICAN) $(CONTENT) -o output -s $(PELICANCONF) -e 'SITEURL="$(LOCAL_SITEURL)"'
	@echo 'URLs in sitemap:' `fgrep '<loc>' < output/sitemap.xml | wc -l`

start-server:
	@echo starting local website server on http://[::]:8000/ ...
	( cd output ;  python -m http.server & )
	@sleep 1

kill-server:
	@pid=`ps -f | egrep -i -- 'python -m http.server' | awk '$$3 == 1 {print $$2;}'` ; \
	if [ -n "$$pid" ] ; then echo kill $$pid ; kill $$pid ; else echo 'no server found' ; fi

clean:
	rm -r output/*

sitemap:
	@token=`cat ${GOOGLE_SEARCH_CONSOLE_ACCESS_TOKEN_FILE}` ;\
	/bin/echo -n 'Sites: ' ; \
	curl -s --request GET \
	  '$(GOOGLE_SEARCH_CONSOLE)/sc-domain:$(URL)' \
	  --header "Authorization: Bearer $$token" \
	  --header 'Accept: application/json' \
	  --compressed | \
	jq -r '.siteUrl,.permissionLevel' | \
	paste - - ; \
	/bin/echo -n 'Sitemap: ' ; \
	curl -s --request GET \
	  '$(GOOGLE_SEARCH_CONSOLE)/sc-domain:$(URL)/sitemaps' \
	  --header "Authorization: Bearer $$token" \
	  --header 'Accept: application/json' \
	  --compressed | \
	jq -r '.sitemap[0]|.path,.type,.lastSubmitted,.lastDownloaded,.warnings,.errors' | \
	paste - - - - - -

sitemap-publish:
	@token=`cat ${GOOGLE_SEARCH_CONSOLE_ACCESS_TOKEN_FILE}` ;\
	curl -s --request PUT \
	  '$(GOOGLE_SEARCH_CONSOLE)/sc-domain:$(URL)/sitemaps/$(SITEMAP)' \
	  --header "Authorization: Bearer $$token" \
	  --header 'Accept: application/json' \
	  --compressed | \
	jq -c .

CHANGELOG.md: .FORCE
	@tmp=/tmp/_$$$$.md ; \
	( \
		cp /dev/null $$tmp ; \
		echo '# Change Log' ; \
		echo '' ; \
		git log --date=iso-local --pretty=format:' - %ci [%h](../../commit/%H) %s' ; \
		echo '' ; \
	)  >> $$tmp ; \
	diff $$tmp CHANGELOG.md || ( cp $$tmp CHANGELOG.md ; echo "CHANGELOG.md - updated" ) ; \
	rm $$tmp
.FORCE:
