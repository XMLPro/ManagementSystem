from django.shortcuts import render_to_response
from django.http import HttpResponse
from system.models import *

def requestView(request):
    return HttpResponse("requestView")


