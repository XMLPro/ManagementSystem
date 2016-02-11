from django.conf.urls import patterns, url
from system.controllers import topView

urlpatterns = [
    url(r'^$', topView.topView),
]
