# rachellevy.uk and associated domains

AUTHOR = 'Rachel Levy'
SITENAME = 'Rachel Levy'
SITESUBTITLE = 'My personal website telling my personal story'
LANDING_PAGE_TITLE = 'Rachel Levy - Holocaust survivor'
SITE_DESCRIPTION = (
    'Rachel Levy - Holocaust survivor'
)

# removed ... really not needed
#AUTHORS = {
#    'Rachel Levy': {
#        'url': 'http://rachellevy.uk',
#        'blurb': 'Rachel Levy',
#    },
#}
#

SITEURL = ''

PATH = "content"

TIMEZONE = "Europe/London"
DATE_FORMATS = {"en": "%b %d, %Y"}
DEFAULT_LANG = "en"

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
        "markdown.extensions.attr_list": {},
    }
}

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'sitemap',
    'share_post',
    'search',
    'related_posts',
    'neighbors',
#    "extract_toc",
#    "liquid_tags.img",
#    "liquid_tags.include_code",
#    "series",
]

THEME = 'themes/elegant'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
     },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily',
     },
    'exclude': [
        '^/noindex/',
        '/tag/',
        '\\.json$',
    ],
}

# URL settings
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Make the homepage a page called 'index'
INDEX_SAVE_AS = "index.html"

DISPLAY_PAGES_ON_MENU = True

RECENT_ARTICLES_COUNT = 10

DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False

# These could have .html at the end ... but with Cloudflare workers, these work ... 
CATEGORIES_URL = 'categories.html'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

SEARCH_URL = 'search.html'

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'search', '404']
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

HOSTED_ON = {"name": "Cloudflare", "url": "https://cloudflare.com/"}

PROJECTS_TITLE = 'Other sites'
PROJECTS = [
  {
    'name': 'Memoir: I Still Dream In Yiddish',
    'url': 'https://myvoice.org.uk/book/i-still-dream-in-yiddish/',
    'description':
      'In 2025, I published my memoir, I Still Dream In Yiddish, as part of the UK-based My Voice project, '
      'a national initiative to preserve and share the life stories of Holocaust survivors living in the United Kingdom.',
  },
  {
    'name': '45 Aid Society - The Boys History',
    'url': 'https://45aid.org/survivors/ruzena-slomovicova/',
    'description':
      'My Subcarpathian Ruthenia roots.',
  },
  {
    'name': '45 Aid Society - The Memory Quilts',
    'url': 'https://45aid.org/quilt-story/rachel-levy/',
    'description':
      'The Memory Quilts are a celebration of the lives of the Boys. '
      'My granddaughter made this quilt square and wrote: '
      '"'
      'This quilt square represents what I pictured in my own mind as my Grandmother described her memories of Behutz to me. '
      'A family owned mill alongside a river, nestled in a green valley – a beloved home to my Grandmother.'
      '"',
  },
]

SOCIAL_PROFILE_LABEL = 'Stay in Touch'
SOCIAL = [
    ('Email', 'rachel@rachellevy.uk', 'My Email Address'),
    ('Facebook', 'https://facebook.com/rachel.levy.754'),
    ('YouTube', 'https://www.youtube.com/@ruzenarachel', 'YouTube Channel')
]

SHARE_POST_INTRO = 'Share me with your friends on'
SHARE_LINKS = [
    ('email', 'Email'),
    ('X', 'X'),
    ('facebook', 'Facebook'),
]

# TEMPLATE_PAGES = {'index.html': 'index.html'}

# Feed settings (optional, can be disabled)
FEED_ALL_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

TYPOGRIFY = True
DEFAULT_PAGINATION = 10

# Static paths if needed
STATIC_PATHS = ['images', 'static']
EXTRA_PATH_METADATA = {
    # "extra/CNAME": {"path": "CNAME"},
    'static/robots.txt': {'path': 'robots.txt'},
}

CUSTOM_CSS = 'static/custom.css'

# stork search
STORK_INPUT_OPTIONS = {
    'base_directory': PATH,
    'url_prefix': SITEURL,
}
STORK_OUTPUT_OPTIONS = {
    'debug': False,
}
