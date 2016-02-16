from django.shortcuts import render_to_response
from system.models import *

from django.http import HttpResponse

def borrow(request):
    equipment_name = request.GET['equipment_name']
    return HttpResponse("borrow: " +equipment_name)

def ret(request):
    equipment_name = request.GET['equipment_name']
    equipment = Equipment.objects.filter(equipment_name = equipment_name)
    for eq in equipment:
      eq.borrower = None
    # Equipment.save()
    return HttpResponse("return: " +equipment_name)

def reserve(request):
    equipment_name = request.GET['equipment_name']
    return HttpResponse("reserve: " +equipment_name)
