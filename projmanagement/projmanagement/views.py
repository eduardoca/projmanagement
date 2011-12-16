'''
Created on 15/12/2011

@author: Educalat
'''
from django.shortcuts import render_to_response
from django.template import RequestContext

def javascript(request, app, js):
    """
    Used to request javascript templates.
    """
    return render_to_response("%s/%s.js" % (app, js),
        context_instance=RequestContext(request))