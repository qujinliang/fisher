"""
 Created by qujl on 2018-04-27
"""
__author__ = 'qujl'

from flask import jsonify
from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook

@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q:
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type':'application/json'}