"""
 Created by qujl on 2018-04-27
"""
__author__ = 'qujl'
from httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        # url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    # 低级错误 每个函数都要加@classmethod
    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result