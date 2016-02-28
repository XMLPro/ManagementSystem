from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from system.controllers.utils import reverse_or_404


def resolve_name_and_title(name, title):
    default_urlname="system:top"
    default_title="トップページ"

    url = reverse_or_404(default_urlname, name)
    if not name and not title:
        title = default_title
    elif not title:
        title = url

    return [url, title]


def finish(message, backname=None, backtitle=None):
    redirect_url = "{url}?message={message}".format(
        url=reverse("system:manage"),
        message=message)
    if backname:
        redirect_url += "&backname=" + backname
    if backtitle:
        redirect_url += "&backtitle=" + backtitle
    return redirect(redirect_url)


def postFinishView(request):
    # リダイレクト先の受け取り
    backurl, backtitle = resolve_name_and_title(
        request.GET.get("backname"),
        request.GET.get("backtitle"))

    # {{ message }}が完了しました！
    # で表示されます
    try:
        # 必要そうなものを列挙
        message = {
            "borrow": "貸出",
            "return": "返却",
            "reserve": "予約",
            "cancel_reserve": "予約の取り消し",
            "vote": "投票",
            "request": "リクエスト",
            "delete": "削除",
            "user_register": "ユーザー登録",
        }[request.GET["message"]]
    except KeyError:
        # 上のリストに無いものが送られてきた場合
        message = "何か"
    return render_to_response("postFinishView.html", RequestContext(request, {
        "message": message,
        "backurl": backurl,
        "backtitle": backtitle,
        }))
