#/apps/languages/
from django.db import models
from django.contrib import admin

from pescalex.apps.languages.models import Language

admin.site.register(Language)