from django.shortcuts import render_to_response
from system.models import Equipment, Reserved
from django.contrib.auth.decorators import *


@login_required
def topView(request):
    equipment_list = Equipment.objects.all()
    for equipment in equipment_list:
        equipment.reserved_num = Reserved.objects.filter(equipment=equipment).count()
        # print(equipment.reserved_num)
    return render_to_response('topView.html', {
        'equipment_list': equipment_list,
        'username': request.user,
    })
