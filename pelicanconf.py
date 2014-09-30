#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = u'themes/pure'

AUTHOR = u'Patrick Snape'
SITENAME = u'patricksnape'
SITEURL = u'http://patricksnape.github.io'
TAGLINE = u'PhD Candidate at Imperial College London'
        

TIMEZONE = u'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (
    (u'github-square', u'https://github.com/patricksnape'),
    (u'google-plus-square', u'https://plus.google.com/+PatrickSnape'),
    (u'twitter-square', u'https://twitter.com/berecursive'),
)

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

PLUGIN_PATHS = [u'plugins']
PLUGINS = [u'gravatar']

DISQUS_SITENAME = u'patricksnape'

PATH = u'content'
PROFILE_IMAGE_URL = u'theme/img/avatar.jpg'
STATIC_PATHS = [u'publications']

ARTICLE_URL = u'{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = u'{date:%Y}/{slug}/index.html'
