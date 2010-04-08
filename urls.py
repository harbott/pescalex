from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Text Pages
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template':'pages/home.html'}, name='home'),
    url(r'^aboutus/$', 'django.views.generic.simple.direct_to_template', {'template':'pages/aboutus.html'}, name='aboutus'),
    url(r'^links/$', 'django.views.generic.simple.direct_to_template', {'template':'pages/links.html'}, name='links'),
    url(r'^contact/$', 'django.views.generic.simple.direct_to_template', {'template':'pages/contact.html'}, name='contact'),
    
    # Apps
    (r'^news/', include('pescalex.apps.news.urls')),
    (r'^glossaries/', include('pescalex.apps.glossaries.urls')),
    (r'^courses/', include('pescalex.apps.courses.urls')),
    (r'^accounts/', include('pescalex.apps.users.urls')),
	
	# Admin
	url('^admin/glossaries/glossary/import/(\d+)/$', 'pescalex.apps.glossaries.admin.import_glossary', name='admin_import_glossary'),
	url('^admin/courses/course/pages/(\d+)/(\d+)/$', 'pescalex.apps.courses.admin.courses_pages', name='admin_courses_pages'),
    url('^admin/courses/course/save_tree/(\d+)/$', 'pescalex.apps.courses.admin.save_tree', name='admin_courses_save_tree'),    
    url('^admin/courses/course/add_page/(\d+)/$', 'pescalex.apps.courses.admin.add_page', name='admin_courses_add_page'),	
    url('^admin/courses/course/remove_page/$', 'pescalex.apps.courses.admin.remove_page', name='admin_courses_remove_page'),
    
    url('^admin/courses/course/get_language_labels/$', 'pescalex.apps.courses.admin.get_language_labels', name='admin_get_language_labels'),	
    url('^admin/courses/course/set_language_label/(\d+)/(\d+)/$', 'pescalex.apps.courses.admin.set_language_label', name='admin_set_language_label'),
    
    url('^admin/courses/course/edit_content/(\d+)/(\d+)/$', 'pescalex.apps.courses.admin.edit_content', name='admin_edit_content'),	
    url('^admin/courses/course/save_content/(\d+)/$', 'pescalex.apps.courses.admin.save_content', name='admin_save_content'),	    
	
    (r'^admin/', include(admin.site.urls)),
)

# Import static url configuration for local development only
if settings.DEBUG:
    urlpatterns += patterns('',
        # Media
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )