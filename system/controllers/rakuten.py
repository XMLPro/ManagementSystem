# coding -*- utf-8 -*-
import json
import requests
from io import StringIO
from system.models import Equipment


class Rakuten():
    __APPLICATION_ID = "1011546524580691339"
    searchResult = None

    def __init__(self, **query):
        self._queryUrl = self._createQueryUrl(**query)


    def _createQueryUrl(self, **query):
        queryUrl = "?applicationId={applicationId}".format(applicationId=self.__APPLICATION_ID)
        for i in query:
            queryUrl += "&{key}={value}".format(key=i, value=query[i])
        return queryUrl


    def setQuery(self, **query):
        self.queryUrl = self._createQueryUrl(**query)


    def search(self):
        response = requests.get(self._url + self._queryUrl)
        response.encoding = response.apparent_encoding
        io = StringIO(response.text)
        self.searchResult = json.load(io)["Items"]


    def getResult(self):
        return self.searchResult


    def getItems(self):
        return [Item(x["Item"]) for x in self.searchResult]


class Item():
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
    _url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522"

    @staticmethod
    def getItem(isbn):
        rakuten = RakutenBooks(isbn=isbn)
        rakuten.search()
        items = rakuten.getItems()
        return items[0] if items else None


class RakutenIchiba(Rakuten):
    _url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222"

    @staticmethod
    def getItem(itemCode):
        rakuten = RakutenIchiba(itemCode=itemCode)
        rakuten.search()
        items = rakuten.getItems()
        return items[0] if items else None
