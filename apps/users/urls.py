#/apps/users/
from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login

urlpatterns = patterns('',
    url(r'^login/$', 'pescalex.apps.users.views.users_login', name='users_login'),   
    url(r'^logout/$', logout_then_login, name='users_logout'),
    url(r'^register/$', 'pescalex.apps.users.views.users_register', name='users_register'),
    url(r'^recover/$', 'pescalex.apps.users.views.users_recover', name='users_recover'),
    url(r'^profile/$', 'pescalex.apps.users.views.users_profile', name='users_profile'),
)