#/apps/courses/
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson

from pescalex.apps.courses.models import Course, CoursePage, CoursePageContent
from pescalex.apps.languages.models import Language

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_languages')
    
    def display_languages(self, obj):
        return ', '. join(str('<a href="' + reverse('admin_courses_pages', args=[obj.id, x.id]) + '">' + str(x) + '</a>') for x in obj.languages.all())
    display_languages.short_description = 'Languages'
    display_languages.allow_tags = True
    
    def save_model(self, request, obj, form, change):
        """ cleanup the languages """
        if change:
            # get the pages for that course.
            course_pages = CoursePage.objects.filter(course=obj)
            languages = form.cleaned_data['languages']
            # remove the content of the language (which are not in 'languages')
            CoursePageContent.objects.exclude(language__in=languages, course_page__in=course_pages).delete()
            
        super(CourseAdmin, self).save_model(request, obj, form, change)            

admin.site.register(Course, CourseAdmin)
admin.site.register(CoursePage)
admin.site.register(CoursePageContent)

def add_page(request, course_id):
    course = Course.objects.get(id=course_id)
    course_page = CoursePage(course=course)
    course_page.save()
    
    for l in course.languages.all():
        CoursePageContent(course_page=course_page, name='New Page...', language=l, content='').save()
    
    return HttpResponse('ok:'+str(course_page.id))

def remove_page(request):
    if request.method == 'POST':
        pages = request.POST.getlist('pages[]')
        #return HttpResponse(pages)
        
        CoursePage.objects.filter(id__in=pages).delete()
        return HttpResponse('ok:')
        
    return HttpResponse('err:Not a post method.')

def save_tree(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)       

        post_tree = request.POST.get('tree', '')
        
        course.serialized_tree = post_tree
        course.save()
        
        return HttpResponse('ok:')
        
    return HttpResponse('err:Not a post method.')        

def get_language_labels(request):    
    # get values...
    pages       = request.GET.getlist('pages[]')
    language_id = request.GET.get('language_id', False)
    
    # check...
    if pages == False or language_id == False:
        return HttpResponse('err:Missing arguments...')
    
    # get the course page and the language.
    course_page         = CoursePage.objects.filter(id__in=pages).all()
    language            = Language.objects.get(id=language_id)
    
    resp = {}
    
    # for each course page get then title and content.
    for cp in course_page:
        course_page_content, created = CoursePageContent.objects.get_or_create(course_page=cp, language=language)
        
        if created:
            course_page_content.name = 'New Page...'
            course_page_content.content = ''
            course_page_content.save()    
        
        #print course_page_content.get_name()
        resp[cp.id] = course_page_content.get_name()
        
    return HttpResponse(simplejson.dumps(resp), mimetype='application/json')

def edit_content(request, page_id, language_id):
    course_page     = CoursePage.objects.get(id=page_id)
    language            = Language.objects.get(id=language_id)
    course_page_content = CoursePageContent.objects.get(course_page=course_page, language=language)
    
    return render_to_response('admin/course_edit_content.html',locals())

def save_content(request, course_page_content_id):
    if request.method == 'POST':
       course_page_content = CoursePageContent.objects.get(id=course_page_content_id)
       course_page_content.content = request.POST.get('new_content', '')
       course_page_content.save()
       return HttpResponse('ok:')
    
    return HttpResponse('err:Not a post method.')

def set_language_label(request, page_id, language_id):
    if request.method == 'POST':
        post_label          = request.POST.get('label', '')
        course_page         = CoursePage.objects.get(id=page_id)
        language            = Language.objects.get(id=language_id)
        course_page_content = CoursePageContent.objects.get(course_page=course_page, language=language)
        course_page_content.name = post_label
        course_page_content.save()
        return HttpResponse('ok:')
    
    return HttpResponse('err:Not a post method.')           

def courses_pages(request, course_id, language_id):
    course = Course.objects.get(id=course_id)
    language = Language.objects.get(id=language_id)
        
    return render_to_response('admin/course_manage_pages.html',locals()) 