from django.conf.urls import patterns, url
from system.controllers import topView
from system.controllers import mypageView
from system.controllers import logView
from system.controllers import requestView
from system.controllers import lendManage

urlpatterns = [
    url(r'^$', topView.topView),
    url(r'^mypage/$', mypageView.mypageView),
    url(r'^log/$', logView.logView),
    url(r'^request/$', requestView.requestView, name='requestView'),
    url(r'^vote/$', requestView.vote, name='vote'),
    # url(r'^lend_manage/borrow/$', lendManage.borrow),
    # url(r'^lend_manage/return/$', lendManage.ret),
    # url(r'^lend_manage/reserve/$', lendManage.reserve),
]
