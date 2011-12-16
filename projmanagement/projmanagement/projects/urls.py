'''
Created on 03/12/2011

@author: eduardo
'''
from django.conf.urls.defaults import url, patterns
from django.views.generic import DetailView
from projmanagement.projects.models import Project
from projmanagement.projects.views import ProjectListView

urlpatterns = patterns('',
    # Examples:
    url(r'^$',
        ProjectListView.as_view(
                         queryset=Project.objects.all(),
                         context_object_name='project_list',
                         template_name='projects/projects.html')), 
    url(r'^(?P<pk>\d+)/$', 
        DetailView.as_view(
                           model=Project,
                           template_name='projects/tasks.html')),                     
    ### AJAX URLS ###
    url(r'^update/$', 'projects.views.update_project', name='update_project'),                                            
)
