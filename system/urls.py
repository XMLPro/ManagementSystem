from django.conf.urls import patterns, url
from system.controllers import topView
from system.controllers import mypageView
from system.controllers import logView
from system.controllers import requestView
from system.controllers import loginView

urlpatterns = [
    url(r'^$', topView.topView),
    url(r'^mypage/$', mypageView.mypageView),
    url(r'^log/$', logView.logView),
    url(r'^request/$', requestView.requestView, name='requestView'),
    url(r'^login/$', loginView.login),
    url(r'^vote/$', requestView.vote, name='vote'),
]
