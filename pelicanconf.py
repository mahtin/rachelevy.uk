AUTHOR = "Rachel Levy"
SITENAME = "Rachel Levy"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"

THEME = "themes/smashing-magazine"

# URL settings
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Make the homepage a page called 'index'
INDEX_SAVE_AS = "index.html"

# Feed settings (optional, can be disabled)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Static paths if needed
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    # "extra/CNAME": {"path": "CNAME"},
}
