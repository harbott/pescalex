# Generic base functions used throughout the app
from django.conf import settings

def format_date(obj):
    if obj.date != '':
        return obj.date.strftime(settings.DATETIME_ADMIN_FORMAT)  
    else:
        return obj.last_login.strftime(settings.DATETIME_ADMIN_FORMAT)
format_date.short_description = 'Date'