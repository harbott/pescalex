#/apps/users/
from django.db import models
from django.contrib import admin

from pescalex.apps.users.models import UserProfile
from pescalex.views import format_date

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'email', 'display_groups', format_date)
    list_filter = ('groups',)
    search_fields = ['first_name', 'last_name', 'email']
    
    def display_name(self, obj):
        return obj.first_name +" "+ obj.last_name  
    display_name.short_description = 'Name'
    
    def display_groups(self, obj):
        return ', '. join(str(x) for x in obj.groups.all())   
    display_groups.short_description = 'Group'
    
admin.site.register(UserProfile, UserProfileAdmin)