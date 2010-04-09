#/apps/glossaries/
from django.shortcuts import get_object_or_404, render_to_response, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q 
from django.core.urlresolvers import reverse

from pescalex.constants import LETTERS
from pescalex.apps.glossaries.models import Glossary, GlossaryTerm
from pescalex.apps.languages.models import Language

def glossary_list(request, glossary_id, language_slug):
    search        = request.GET.get('search', 'a')
    term_id       = request.GET.get('term', '1')
    #language    = request.GET.get('language', '1')
    language    = get_object_or_404(Language, slug=language_slug)
    
    # Get results pane
    results = GlossaryTerm.objects.filter(glossary=glossary_id, language=language.id)    # Filter by glossary and language
    
    if len(search) > 1:
		# Free text search 
		results = results.filter(
            Q(term__icontains=search) |
			Q(definition__icontains=search)
		)
    else:
		a = search
		# Search first letter of term
		results = results.filter(
			term__istartswith = search
		)
    
    # Search term
    term = get_object_or_404(GlossaryTerm, term_id=term_id, glossary=glossary_id, language=language.id)
     
    alphabet = LETTERS
    
    return render_to_response('glossaries/list.html', locals())