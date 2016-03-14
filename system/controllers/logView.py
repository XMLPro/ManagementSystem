from django.shortcuts import render_to_response
from system.models import Log
from django.template import RequestContext
from system.controllers.search import search_log


def logView(request):
    keywords = ""
    if 'keywords' in request.POST and request.POST["keywords"] != "":
        keywords = request.POST["keywords"]
        log_list = search_log.search(keywords)
    else:
        log_list = Log.objects.all()
    return render_to_response("logView.html", RequestContext(request, {
        "log_list": log_list,
        "keywords": keywords,
    }))
