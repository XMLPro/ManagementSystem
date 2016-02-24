from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from system.controllers.postFinishView import finish
from system.models import Reserved, Equipment


def reservePost(request):
    if request.method == "POST":
        equipment = Equipment.objects.get(id=request.POST["equipment_id"])
        reserve = Reserved(equipment=equipment, user=request.user)
        reserve.save()
        return finish("reserve")
    return redirect(reverse("system:top"))


def cancelPost(request):
    if request.method == "POST":
        equipment = Equipment.objects.get(id=request.POST["equipment_id"])
        reserved = Reserved.objects.get(equipment=equipment, user=request.user)
        if reserved:
            reserved.delete()
        return finish("cancel_reserve")
    return redirect(reverse("system:top"))
