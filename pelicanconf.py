#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'adrn'
SITENAME = u'in the cold waste'
SITESUBTITLE = u'<a href="http://adrian.pw">adrn</a>'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://github.com/adrn'),
          ('Twitter', 'https://twitter.com/adrianprw'),
          ('Linkedin', 'https://www.linkedin.com/profile/view?id=318215201&trk=nav_responsive_tab_profile_pic'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Themes
THEME = 'pelican-themes/aboutwilson'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['latex', 'neighbors', 'summary']

# Only use LaTeX for selected articles
LATEX = 'article'
