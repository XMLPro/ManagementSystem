from django.shortcuts import render_to_response
from system.models import Log
from django.template import RequestContext


def logView(request):
    log_list = Log.objects.all()
    return render_to_response("logView.html", RequestContext(request, {
        "log_list": log_list,
            }))
