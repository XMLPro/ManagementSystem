from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from system.controllers.rakuten import RakutenBooks


def addEquipmentView(request):
    if request.method == "POST":
        RakutenBooks.getItem(
                request.POST.get("equipmentIsbn")).createEquipment().save()
        return render_to_response("postFinishView.html", RequestContext(
            request, {
                "message": "備品登録",
                "backurl": reverse("system:addEquipment"),
                "backtitle": "備品登録ページ",
            }))

    items = []
    error = ""
    if request.GET and (
            request.GET.get("keyword") or
            request.GET.get("author") or
            request.GET.get("publisher") or
            request.GET.get("isbn")
            ):
        rakutenApi = RakutenBooks(
                title=request.GET.get("keyword"),
                author=request.GET.get("author"),
                publisherName=request.GET.get("publisher"),
                isbn=request.GET.get("isbn")
                )
        rakutenApi.search()
        items = rakutenApi.getItems()
        items = [x.createEquipment() for x in items]

        if not items:
            error = "検索結果が見つかりませんでした。"

    return render_to_response("addEquipmentView.html", RequestContext(
        request, {
            "items": items,
            "error": error,
        }))
