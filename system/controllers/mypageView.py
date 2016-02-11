from django.shortcuts import render_to_response
from system.models import *

def mypageView(request):
    my_list = []
    my_reserved = []
    return render_to_response('mypageView.html',{
        'my_list': my_list,
        'my_reserved': my_reserved,
        })

