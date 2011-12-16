from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from projmanagement.projects.forms import ProjectForm
from projmanagement.projects.models import Project


class ProjectListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        pr = Project.objects.get(pk=1)
        context['form'] = ProjectForm(instance=pr)
        context['project'] = pr 
        
        return context

def update_project(request):
    """
    AJAX client sends a serialized form by POST. ID comes from the article_id key.
    
    The function returns JSON, either the updated Article object, or the form's
    error dict.
    """
    try:
        project_id = int(request.POST['project_id'])
    except KeyError:
        raise Http404
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(request.POST, instance=project)
    if form.is_valid():
        form.save()
        return HttpResponse(serializers.serialize('json', (project,)), mimetype="application/json")
    else:
        return HttpResponse(serializers.serialize('json', form.errors), mimetype="application/json")