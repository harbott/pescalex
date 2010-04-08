#/apps/news/
from django.conf.urls.defaults import *

from pescalex.apps.news.models import News

news_info = {
    "queryset" : News.objects.filter(published = True).all(),
    "template_object_name" : "news",
}

urlpatterns = patterns('',
    url(r'^list/$',                                        'django.views.generic.list_detail.object_list',        dict(news_info, template_name='news/list.html'),     name='news_list'),
    url(r'^article/(?P<object_id>\d+)/$',    'django.views.generic.list_detail.object_detail',   dict(news_info, template_name='news/detail.html'), name='news_article'),
)