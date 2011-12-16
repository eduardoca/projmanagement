from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

# To enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^js/([\w\.\-]+)/([\w\.\-]+)/$', 'views.javascript', name='javascript'),                       
    url(r'^projects/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()