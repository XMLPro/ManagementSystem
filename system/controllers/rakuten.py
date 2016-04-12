# coding -*- utf-8 -*-
import json
import requests
from io import StringIO
from system.models import Equipment


class Rakuten():
    """このクラスは、RakutenBooks, RakutenIchibaのクラスの親クラスです。

    楽天apiを使用する際はそちらを使用してください。"""

    __APPLICATION_ID = "1011546524580691339"
    searchResult = None

    def __init__(self, **query):
        self._queryUrl = self._createQueryUrl(**query)

    def _createQueryUrl(self, **query):
        queryUrl = "?applicationId={applicationId}".format(
                applicationId=self.__APPLICATION_ID
                )
        for i in query:
            if query[i]:
                queryUrl += "&{key}={value}".format(key=i, value=query[i])
        return queryUrl

    def setQuery(self, **query):
        self.queryUrl = self._createQueryUrl(**query)

    def search(self):
        response = requests.get(self._url + self._queryUrl)
        response.encoding = response.apparent_encoding
        io = StringIO(response.text)
        searchResult = json.load(io).get("Items")
        self.searchResult = searchResult if searchResult else []

    def getResult(self):
        return self.searchResult

    def getItems(self):
        return [Item(x["Item"]) for x in self.searchResult]


class Item():
    """このクラスは、楽天apiの検索結果からgetItemsで取得出来ます。

    Equipment作成時は、このクラスを使用します。
    createEquipment()でEquipmentモデルを取得出来るので、それに対しsave()を実行してください。
    """

    def __init__(self, item):
        self.item = item

    def get(self, info):
        return self.item[info]

    def createEquipment(self):
        return Equipment(
                equipment_name=self.get("title"),
                author=self.get("author"),
                company=self.get("publisherName"),
                price=self.get("itemPrice"),
                isbn=self.get("isbn"),
                product_url=self.get("itemUrl"),
                image_url=self.get("mediumImageUrl")
                )


class RakutenBooks(Rakuten):
    """このクラスは、楽天ブックス書籍検索apiを使うためのクラスです。

    以下、簡単な使用法です。
    raku = RakutenBooks(title="java") のようにクエリを指定します。
    raku.search() ここで楽天apiにリクエストを送信します。
    raku.getItems() Itemオブジェクトが配列で渡されます。
    """

    _url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522"

    @staticmethod
    def getItem(isbn):
        rakuten = RakutenBooks(isbn=isbn)
        rakuten.search()
        items = rakuten.getItems()
        return items[0] if items else None


class RakutenIchiba(Rakuten):
    """このクラスは、楽天商品検索apiを使うためのクラスです。

    以下、簡単な使用法です。
    raku = RakutenBooks(keyword="java") のようにクエリを指定します。
    raku.search() ここで楽天apiにリクエストを送信します。
    raku.getItems() Itemオブジェクトが配列で渡されます。
    """

    _url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222"

    @staticmethod
    def getItem(itemCode):
        rakuten = RakutenIchiba(itemCode=itemCode)
        rakuten.search()
        items = rakuten.getItems()
        return items[0] if items else None


def sample1():
    # equipmentモデル適当作成
    raku = RakutenBooks(title="java")
    raku.search()
    items = raku.getItems()
    for item in items:
        print(item.get("title"))
        item.createEquipment().save()

    print(" - - - - - - - - - - ")


def sample2():
    # isbnからequipmentモデル作成
    item = RakutenBooks.getItem(9784774171302)
    print(item.get("title"), item.get("author"), item.get("publisherName"))
    item.createEquipment().save()

    print(" - - - - - - - - - - ")