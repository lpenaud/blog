AUTHOR = 'PENAUD Loïc'
SITENAME = 'PENAUD Loïc blog'
SITEURL = ""

PATH = "content"

THEME = "themes/pelican-theme"
CSS_FILE = "main.css"
JS_FILES = ("nav.js",)

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Nav menu
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = False

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
