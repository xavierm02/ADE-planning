from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$|^/$|^index.html$', 'application.views.home'),
    url(r'^.*$', 'application.views.proxy')
)
