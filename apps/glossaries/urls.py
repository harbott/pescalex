#/apps/glossaries/
from django.conf.urls.defaults import *

from pescalex.apps.glossaries.models import Glossary, GlossaryTerm
from pescalex.apps.glossaries.views import glossary_list

urlpatterns = patterns('',
    url(r'^search/(?P<glossary_id>\d+)/(?P<language_slug>\w+)/$', glossary_list, name='glossary_list')
)