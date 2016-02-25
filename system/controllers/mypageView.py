from django.shortcuts import render_to_response
from django.template import RequestContext
from system.models import Equipment, Reserved


def mypageView(request):
    borrower_list = Equipment.objects.filter(borrower=request.user.id)
    for borrower_item in borrower_list:

        count = Reserved.objects.filter(equipment=borrower_item).count()
        setattr(borrower_item, 'num', count)

    reserved_list = Reserved.objects.filter(user=request.user.id)

    ctxt = RequestContext(request, {
        'borrower_list': borrower_list,
        'reserved_list': reserved_list,
        })
    return render_to_response('mypageView.html', ctxt)
