from django.conf.urls import patterns, url
from system.controllers import topView
from system.controllers import mypageView
from system.controllers import logView
from system.controllers import requestView
from system.controllers import borrowReturnPost, reservePost, postFinishView
from system.controllers import userRegister

urlpatterns = [
    url(r'^$', topView.topView, name='top'),
    url(r'^user_register/$', userRegister.userRegister,
        name='user_register'),
    url(r'^user_register/finish$', userRegister.finishUserRegisterView,
        name='finish_register'),
    url(r'^mypage/$', mypageView.mypageView, name='mypage'),
    url(r'^log/$', logView.logView, name='log'),
    url(r'^request/$', requestView.requestView, name='requestView'),
    url(r'^vote/$', requestView.vote, name='vote'),

    url(r'^manage/borrow/$', borrowReturnPost.borrowPost,
        name='manage-borrow'),
    url(r'^manage/return/$', borrowReturnPost.returnPost,
        name='manage-return'),

    url(r'^manage/reserve/$', reservePost.reservePost,
        name='manage-reserve'),
    url(r'^manage/cancel_reserve/$', reservePost.cancelPost,
        name='manage-cancel'),

    url(r'^manage/$', postFinishView.postFinishView, name='manage'),
    url(r'^tag_add/$', topView.ajax_tag_add, name='tag_add'),
]
