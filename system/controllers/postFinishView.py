from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def finish(message):
    return redirect(reverse("system:manage")+"?message="+message)


def postFinishView(request):
    # {{ message }}が完了しました！
    # で表示されます
    try:
        # 必要そうなものを列挙
        # 自分が使ったのは2個のみ
        message = {
            "borrow": "貸出",
            "return": "返却",
            "reserve": "予約",
            "cancel_reserve": "予約の取り消し",
            "vote": "投票",
            "request": "リクエスト",
            "delete": "削除",
        }[request.GET["message"]]
    except KeyError as e:
        # 上のリストに無いものが送られてきた場合
        message = "何か"
    return render_to_response("postFinishView.html", RequestContext(request, {
        "message": message,
        }))
