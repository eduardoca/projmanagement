'''
Created on 15/12/2011

@author: Educalat
'''
from django.forms import ModelForm
from projmanagement.projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        
        