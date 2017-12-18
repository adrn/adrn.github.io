#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'adrn'
SITENAME = u'adrian price-whelan'
# SITESUBTITLE = u'<a href="http://adrian.pw">adrn</a>'

# THEME = 'pelican-themes/aboutwilson'
THEME = 'themes/apw'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Social widget
# SOCIAL = (('Github', 'https://github.com/adrn'),
#           ('Twitter', 'https://twitter.com/adrianprw'),
#           ('googlescholar', 'http://scholar.google.ca/citations?user=_wSmxLcAAAAJ&hl=en'))

STATIC_PATHS = [
    'blog/static',
    'pages/images',
    'extra/'
]
EXTRA_PATH_METADATA = {
    'extra/README.md': {'path': 'README.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

MENUITEMS = [('bio', 'bio.html'),
             ('cv', 'https://github.com/adrn/cv/raw/master-pdf/cv.pdf'),
             ('research', 'research.html'),
             ('code', 'code.html'),
             ('teaching', 'teaching.html'),
             ('blog', 'blog/')]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'Uncategorized'

DEFAULT_PAGINATION = 8
RELATIVE_URLS = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

PAGE_PATHS = ['pages']
PAGE_URL = '../{slug}.html'
PAGE_SAVE_AS = '../{slug}.html'


# Blog stuff: Formatting for urls
ARTICLE_PATHS = ['blog']
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

INDEX_SAVE_AS = "blog/index.html"
AUTHOR_URL = False
AUTHOR_SAVE_AS = False
AUTHORS_URL = False
AUTHORS_SAVE_AS = False

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['latex', 'liquid_tags.notebook', 'summary']

DISQUS_SITENAME = "adrian price-whelan"
GOOGLE_ANALYTICS = "UA-11936482-16"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False

NOTEBOOK_DIR = "blog/notebooks"
