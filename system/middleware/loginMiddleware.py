from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
ALLOWED_EXEMPT_URLS = None
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]
if hasattr(settings, 'ALLOWED_EXEMPT_URLS'):
    ALLOWED_EXEMPT_URLS = [compile(expr) for expr in settings.ALLOWED_EXEMPT_URLS]


class LoginMiddleware:
    """
    このミドルウェアは以下のサイトを基に作られています。
    http://hateda.hatenadiary.jp/entry/2014/01/27/151615
    よろしければ参考にどうぞ


    LOGIN_URL 以外のページでユーザ認証を要求するミドルウェア。
    ユーザ認証を免除するページは、 LOGIN_EXEMPT_URLS に正規表現で指定する
    必要がある。（これを urls.py にコピーすることもできる）
    ログイン要求ミドルウェアとコンテキストプロセッサーのテンプレートが
    読み込まれる。読み込まれなかった場合、エラーが発生するかもれない。

    追加機能として、ALLOED_EXMPT_URLS以外のページでユーザー認証を判定できる。
    Userモデルのis_validが有効でない場合すなわち登録要求はしているが管理者が有効にしていない場合は
    ALLOWED_URLに飛ばすことである。
    """

    def process_request(self, request):
        assert hasattr(request, 'user'), "ログイン要求ミドルウェア\
はユーザ認証ミドルウェアのインストールを要求します。MIDDLEWARE_CLASSES を\
編集して、'django.contrib.auth.middlware.AuthenticationMiddleware' を\
追加してください。動作しない場合、 TEMPLATE_CONTEXT_PROCESSORS 設定が\
'django.core.context_processors.auth' に読み込まれていることを\
確認して下さい。"

        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)
        elif not request.user.is_valid:
            # 許可されていないユーザーかどうかを判定する
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in ALLOWED_EXEMPT_URLS):
                print('not allowed')
                print(request.user.is_valid)
            else:
                print('allowed')
                print(request.user.is_valid)
