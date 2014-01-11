#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Avoid having hard coded paths to these files
base_path = os.path.dirname(os.path.realpath(__file__))
THEME = '{}/themes/pelican-responsive/responsive'.format(base_path)

AUTHOR = u'Patrick Snape'
SITENAME = u'patricksnape.github.io'
SITEURL = 'http://patricksnape.github.io'
MINI_BIO = u"PhD Candidate at Imperial College London"
BIO = u"""I am currently working towards
my PhD at Imperial College London. I'm a member of the
<strong>I</strong>ntelligent <Strong>B</strong>ehaviour
<strong>U</strong>nderstanding <strong>G</strong>roup
(IBUG), focusing on dense reconstruction of facial shape
from images. In particular, I'm interested in investigating
the low-rank relationship between images and shape."""
        

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/patricksnape', '&#xe037;'),
    ('Google Plus', 'https://plus.google.com/+PatrickSnape', '&#xe039;'),
    ('Twitter', 'https://twitter.com/berecursive', '&#xe086;'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


PLUGIN_PATH = 'plugins'
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.include_code']
LIQUID_TAGS_IPYTHON_STYLES = open('_nb_header.html').read().decode('utf-8')

PATH = '{}/content'.format(base_path)
STATIC_PATHS = ['images', 'code', 'notebooks', 'theme/img/avatar.jpg']
