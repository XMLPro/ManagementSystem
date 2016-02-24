from django.shortcuts import render_to_response
from system.models import Equipment, Reserved
from django.template import RequestContext
from django.core.urlresolvers import reverse
from system.controllers.search import search


class Button:
    """ topView.htmlで使用されている、備品の貸出制御ボタン """
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __str__(self):
        return self.name


# Buttonクラスを作成する関数
# これらはcreate_buttonから使用される


def create_borrow_button():
    # return Button("/system/manage/borrow/", "借")
    return Button(reverse("system:manage-borrow"), "借用")


def create_reserve_button():
    return Button(reverse("system:manage-reserve"), "予約")


def create_return_button():
    return Button(reverse("system:manage-return"), "返却")


def create_finish_button():
    return Button(reverse("system:manage-cancel"), "取消")


def create_button(equipment, username):
    # [ 返えす ]
    # 備品を借りている人の名前と、自分の名前が一致
    if equipment.borrower == username:
        return create_return_button()

    # [ 借りる ]
    # 借りてる人がおらず、予約者がおり、自分の名前と一致
    reserved = Reserved.objects.filter(equipment=equipment)
    if not equipment.borrower and reserved and reserved[0].user == username:
        return create_borrow_button()

    # [ 済み ]
    # 予約者に自分の名前が含まれている
    if str(username) in [str(x.user) for x in reserved]:
        return create_finish_button()

    # [ 予約 ]
    # 予約者が存在する
    if reserved:
        return create_reserve_button()

    # [ 借りる ]
    # 借りているがいない
    if not equipment.borrower:
        return create_borrow_button()

    # [ 予約 ]
    # それ以外
    return create_reserve_button()


def topView(request):
    ctxt = RequestContext(request, {})
    keywords = ""
    if 'keywords' in request.POST:
        keywords = search(request.POST["keywords"])
        equipment_list = keywords
    else:
        equipment_list = Equipment.objects.all()
    # equipmentにフィールド追加
    # .reserved_num: 予約者人数
    # .button:       備品の貸出制御ボタン
    res_objs = Reserved.objects
    for equipment in equipment_list:
        equipment.reserved_num = res_objs.filter(equipment=equipment).count()
        equipment.button = create_button(equipment, request.user)

    return render_to_response('topView.html', {
        'equipment_list': equipment_list,
        'username': request.user,
        'keywords': keywords,
    }, ctxt)
