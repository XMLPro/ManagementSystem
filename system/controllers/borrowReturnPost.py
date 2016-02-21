from django.shortcuts import render_to_response, redirect
from django.utils import timezone
from system.models import Equipment, Reserved, Log
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime
from system.controllers.postFinishView import finish


def borrowPost(request):
    # [ 貸出処理 ]を行います
    # equipmentにborrwerの登録、Lend_countの増加
    # 新しくlog作成、既存のlogがあった場合の処理(不正データ)
    # 予約順番の次が自分だった場合のreserved削除

    try:
        equipment = Equipment.objects.get(id=request.POST["equipment_id"])
    except:
        # postにequipmentが入っていなかった場合
        return redirect("system:top")

    # [ equipmentのデータを処理 ]
    equipment.borrower = request.user
    equipment.Lend_count += 1
    equipment.save()
    try:
        # [ 不正データの処理 ]
        # 貸出処理しているにも関わらずborrowerがいた時の処理
        log = Log.objects.filter(equipment=equipment, return_date=None)[0]
        # Logの貸出中の表示を1111年1月1日で上書き
        log.return_date = datetime.datetime(1111, 1, 1)
        log.save()
    except IndexError:
        pass

    # [ log作成 ]
    log = Log(user=request.user, equipment=equipment)
    log.save()
    try:
        reserved = Reserved.objects.filter(equipment=equipment)[0]
        if reserved.user == request.user:
            reserved.delete()
    except IndexError:
        pass
    return finish("borrow")


def returnPost(request):
    # [ 返却処理 ]を行います 
    # equipmentのborrowerを空にする
    # logに返却日を記載

    try:
        equipment = Equipment.objects.get(id=request.POST["equipment_id"])
    except:
        # postにequipmentが入っていなかった場合
        return redirect("system:top")

    # [ equipmentのborrowerを空に ]
    borrower = equipment.borrower
    equipment.borrower = None
    equipment.save()

    # [ logに返却日を記載 ]
    try:
        log = Log.objects.get(equipment=equipment, return_date=None)
    except Log.MultipleObjectsReturned as e:
        # 複数の人が同じequipmentを借りている状態の場合

        # 後ろから一件取得　[-1:]が使えませんでした
        log = Log.objects.filter(equipment=equipment, user=borrower, return_date=None)[::-1][0]
    except Log.DoesNotExist as e:
        # 貸したはずのequipmentがLogに無い場合

        log = None

    if log:
        log.return_date = timezone.now()
        log.save()

    return finish("return")
