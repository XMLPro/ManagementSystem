from django.conf.urls import patterns, url

urlpatterns = patterns('system.controllers', 
        url(r'^$', 'topView.topView'),
)
