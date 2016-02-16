from django.shortcuts import render_to_response
from system.models import Equipment, Reserved
from django.template import RequestContext

def topView(request):
    ctxt = RequestContext(request, {})
    equipment_list = Equipment.objects.all()
    for equipment in equipment_list:
        equipment.reserved_num = Reserved.objects.filter(equipment=equipment).count()
        # print(equipment.reserved_num)
    return render_to_response('topView.html', {
        'equipment_list': equipment_list,
        'username': request.user,
    }, ctxt)
