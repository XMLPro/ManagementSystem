from django.template import RequestContext
from system.models import Equipment
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers

def search(request):
    keyword = request.GET["keyword"]
    if keyword == '':
        print("noe")
        result = Equipment.objects.all()
    else:
        print("els")
        result = Equipment.objects.filter(equipment_name=keyword)
    res = serializers.serialize('json', result)
    return HttpResponse(res, content_type='text/javascript')

def view(request):
    ctxt = RequestContext(request)
    return render_to_response('search.html', ctxt)
