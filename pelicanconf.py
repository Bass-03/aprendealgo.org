#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Edmundo Sánchez'
SITENAME = 'AprendeAlgo.org'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'es'
#My settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SITESUBTITLE = "Aprende conmigo"
GITHUB_URL = "https://github.com/gdledsan/aprendealgo.org"
DEFAULT_DATE = 'fs'
DEFAULT_METADATA = {
    'author': 'Edmundo Sánchez',
}
#themes
THEME_STATIC_DIR = 'themes'
THEME = 'themes/nmi'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/gdledsan'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
