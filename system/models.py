from django.db import models
from django.contrib.auth.models import AbstractUser
from ManagementSystem import settings


# [ 備品テーブル ]
# (id), 備品名, 借用者(ユーザーid(外部キー)), 借りた日, 貸出し回数
class Equipment(models.Model):
    equipment_name = models.CharField(max_length=50)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL)
    borrowed_date = models.DateField(auto_now=True)
    Lend_count = models.IntegerField(default=0)

    def __str__(self):
        return self.equipment_name


# [ 検索用テーブル ]
# 備品id(外部キー), 検索用メタデータ
class Search(models.Model):
    equipment_name = models.ForeignKey(Equipment)
    meta_data = models.CharField(max_length=50)

    def __str__(self):
        return str(self.equipment_name) + ": " + self.meta_data


# [ 予約テーブル ]
# 備品id(外部キー), ユーザーid(外部キー), 予約日
class Reserved(models.Model):
    equipment = models.ForeignKey(Equipment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    reserved = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.equipment)


# [ リクエストテーブル ]
# (id), 商品名, AmazonURL, 一言コメント
class Request(models.Model):
    request_name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.request_name


# [ リクエストサブテーブル(投票集計) ]
# リクエストid(外部キー), ユーザーid(外部キー)
class Vote(models.Model):
    request = models.ForeignKey(Request)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.request)


# [ 貸出しログ ]
# 借りた人(ユーザーid(外部キー)), 借りた物(備品id(外部キー)), 借りた日付
class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    equipment = models.ForeignKey(Equipment)
    borrowed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
