# Create your views here.

# django imports
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

# local imports
from pescalex.apps.courses.models import Course, CoursePageContent


def course_view(request, course_id, language_id, page_id=0):
    try:
        language_id = int(language_id)
        course = Course.objects.get(id=course_id)
        
        # this is the redirect to use the first available language.
        if language_id == 0:
            language_id = course.languages.all()[0].id
            return HttpResponseRedirect(reverse('course_view', args=[course_id, language_id]))
        
        # are we actually loading the content of the page as well?
        page_content = False        
        if page_id != 0:
            page_content = CoursePageContent.objects.get(course_page=page_id, language=language_id).content
            
        
        return render_to_response('courses/view_course.html', locals(), context_instance=RequestContext(request))
    except Course.DoesNotExist:
        return HttpResponseRedirect('/') # just forward to home page....
