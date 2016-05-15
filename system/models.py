fom django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_valid = models.BooleanField(default=False)


# [ 備品テーブル ]
# (id), 備品名, 借用者(ユーザーid(外部キー)), 借りた日, 貸出し回数
class Equipment(models.Model):
    equipment_name = models.CharField(max_length=50)
    borrower = models.ForeignKey(CustomUser, null=True, blank=True)
    borrowed_date = models.DateField(auto_now=True)
    Lend_count = models.IntegerField(default=0)

    author = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(default=0)
    isbn = models.CharField(max_length=50, null=True, blank=True)
    product_url = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)

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
    user = models.ForeignKey(CustomUser)
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
    user = models.ForeignKey(CustomUser)

    def __str__(self):
        return str(self.request)


# [ 貸出しログ ]
# 借りた人(ユーザーid(外部キー)), 借りた物(備品id(外部キー)), 借りた日付
class Log(models.Model):
    user = models.ForeignKey(CustomUser)
    equipment = models.ForeignKey(Equipment)
    borrowed_date = models.DateField(auto_now=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


# [タグ用のテーブル]
# [id, タグ名]
class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.tag_name)


# [タグと備品の紐付け用のテーブル]
# 備品名(備品id(外部キー)), タグ名
class TagManagement(models.Model):
    equipment = models.ForeignKey(Equipment)
    tag = models.ForeignKey(Tag)
