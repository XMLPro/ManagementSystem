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
    keyword = request.GET.get("keyword")
    author = request.GET.get("author")
    publisher = request.GET.get("publisher")
    isbn = request.GET.get("isbn")
    if request.GET and (
            keyword or
            author or
            publisher or
            isbn):
        rakutenApi = RakutenBooks(
                title=keyword,
                author=author,
                publisherName=publisher,
                isbn=isbn
                )
        rakutenApi.search()
        items = rakutenApi.getItems()
        items = [x.createEquipment() for x in items]

        if not items:
            error = "検索結果が見つかりませんでした。"

    return render_to_response("addEquipmentView.html", RequestContext(
        request, {
            "keyword": keyword,
            "author": author,
            "publisher": publisher,
            "isbn": isbn,
            "items": items,
            "error": error,
        }))
