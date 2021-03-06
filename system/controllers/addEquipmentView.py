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
    if isbn:
        item = RakutenBooks.getItem(isbn)
        if item:
            items.append(item.createEquipment())
        else:
            error = "検索結果が見つかりませんでした。"
    elif request.GET and (
            keyword or
            author or
            publisher):
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
            "keyword": keyword if keyword else "",
            "author": author if author else "",
            "publisher": publisher if publisher else "",
            "isbn": isbn if isbn else "",
            "items": items,
            "error": error,
        }))
