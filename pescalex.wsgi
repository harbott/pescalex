#!/usr/local/bin/python
import os, sys
sys.path.append('/var/vhosts/')
sys.path.append('/var/vhosts/pescalex/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'  # this is your settings.py file
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
