from django.shortcuts import render_to_response
from system.models import Log
from django.template import RequestContext
from system.controllers.search import search


def logView(request):
    if 'keyword' in request.POST:
        equipment_list = search(request.POST["keyword"])
        log_list = Log.objects.filter(equipment__in=equipment_list
                             ).order_by("borrowed_date")
    else:
        log_list = Log.objects.all()
    return render_to_response("logView.html", RequestContext(request, {
        "log_list": log_list,
            }))
