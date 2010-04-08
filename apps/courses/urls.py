#/apps/glossaries/
from django.conf.urls.defaults import *

from pescalex.apps.courses.views import course_view
urlpatterns = patterns('',
    url(r'^view/(\d+)/(\d+)/(\d+)/$', course_view, name='course_view'),  
    url(r'^view/(\d+)/(\d+)/$', course_view, name='course_view'),  

)