#/apps/news/
from django.db import models
from django.contrib import admin

from pescalex.apps.news.models import News
from pescalex.views import format_date

class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', format_date, 'published')
    list_filter = ('date', 'published', 'author')
    search_fields = ['headline', 'author__first_name', 'author__last_name']
    actions = ['mark_published', 'mark_unpublished']
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js',
            '/media/plugins/tinymce/jquery.tinymce.js',
            '/media/plugins/tinymceadmin/textareas.js',
        )
    
    def mark_published(self, request, queryset):
        rows_updated = queryset.update(published=True)
        message = "%s article(s) were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message)
        
    mark_published.short_description = "Mark as published"
    
    def mark_unpublished(self, request, queryset):
        rows_updated = queryset.update(published=False)
        message = "%s article(s) were" % rows_updated
        self.message_user(request, "%s successfully marked as unpublished." % message)
        
    mark_unpublished.short_description = "Mark as unpublished"

admin.site.register(News, NewsAdmin)