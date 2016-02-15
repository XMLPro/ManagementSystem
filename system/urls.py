from django.conf.urls import patterns, url
from system.controllers import topView
from system.controllers import mypageView
from system.controllers import logView
from system.controllers import requestView

urlpatterns = [
    url(r'^$', topView.topView),
    url(r'^mypage/$', mypageView.mypageView),
    url(r'^log/$', logView.logView),
    url(r'^request/$', requestView.requestView),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}),
]
