from django.shortcuts import render_to_response
from django.http import HttpResponse
from system.models import *

def mypageView(request):
    return HttpResponse("mypageView")

