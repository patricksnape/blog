#!/usr/bin/env python
THEME = "themes/pure"

AUTHOR = "Patrick Snape"
SITENAME = "patricksnape"
SITEURL = "http://patricksnape.github.io"
TAGLINE = "Computer Vision and Machine Learning Engineer"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GOOGLE_ANALYTICS = True
DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (
    ("fa fa-github-square fa-3x", "https://github.com/patricksnape"),
    ("ai ai-google-scholar-square ai-3x",
     "https://scholar.google.com/citations?hl=en&user=L-sUZmUAAAAJ"),
    ("fa fa-twitter fa-3x", "https://twitter.com/berecursive"),
    ("fa fa-linkedin fa-3x", "https://www.linkedin.com/in/patrick-snape/"),
)

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["gravatar"]

PATH = "content"
PROFILE_IMAGE_URL = "theme/img/avatar.jpg"
STATIC_PATHS = ["publications"]

ARTICLE_URL = "{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{slug}/index.html"
