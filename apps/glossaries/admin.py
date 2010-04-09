#/apps/glossaries/
from django.db import models
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from django.conf import settings

from pescalex.apps.glossaries.models import Glossary, GlossaryTerm
from pescalex.apps.languages.models import Language

import uuid
import csv
import os 
import datetime

@csrf_exempt
def import_glossary(request, id):
    # Process excel file and import
    item = Glossary.objects.get(id=id)
            
    if request.POST:    
        if request.FILES['excel'].content_type != 'text/csv':
            error = True
        else:
            file_path = settings.FILE_UPLOAD_TEMP_DIR + str(uuid.uuid4()) +".csv"
            language = request.POST['language']
    
            # Write file to disk
            destination = open(file_path, 'wb+')
            for chunk in request.FILES['excel'].chunks():
                destination.write(chunk)
            destination.close()
            
            # Remove glossary entries
            GlossaryTerm.objects.filter(glossary=id, language=language).delete()
            
            # Open file for processing
            reader = csv.reader(open(file_path, 'rU'), dialect='excel')
            for row in reader:
                if len(row) >= 2:
                    term_id = unicode(str.strip(row[0]), 'utf8')
                    term = unicode(str.strip(row[1]), 'utf8')
                    definition = unicode(row[2], 'utf8')
                    
                    # Add line to db
                    row = GlossaryTerm()
                    row.term_id = term_id
                    row.language = Language(id=language)
                    row.term = term
                    row.definition = definition
                    row.glossary = Glossary(id=id)
                    row.added_at = datetime.datetime.now()
                    row.save(force_insert=True)
                
            # Once complete remove the file
            os.remove(file_path)
            
            return HttpResponseRedirect('../../')            
        
    return render_to_response('admin/import_glossary.html', locals())
        
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_languages', 'display_import_link')
    
    def display_languages(self, obj):
        return ', '. join(str(x) for x in obj.languages.all())   
    display_languages.short_description = 'Languages'
    
    def display_import_link(self, obj):
        return '<a href="'+reverse('admin_import_glossary', args=[obj.id])+'">Import</a>'
    display_import_link.short_description = 'Import Excel'
    display_import_link.allow_tags = True
    
admin.site.register(Glossary, GlossaryAdmin)