from django.shortcuts import render_to_response
from system.models import CustomUser, Equipment, Reserved

def mypageView(request):
    borrower_list = Equipment.objects.filter(borrower=request.user.id)
    for borrower_item in borrower_list:
        count = Reserved.objects.filter(equipment=borrower_list).count()
        setattr(borrower_item, 'num', count)
    reserved_list = Reserved.objects.filter(user=request.user.id)
    return render_to_response('mypageView.html',{
        'borrower_list': borrower_list,
        'reserved_list': reserved_list,
        })
