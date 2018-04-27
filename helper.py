"""
 Created by qujl on 2018-04-27
"""
__author__ = 'qujl'

def is_isbn_or_key(word):
    """
    :param word:
    :return:
    isbn isbn13 13个0到9的数字组成
    isbh10 10个0到9的数字组成，含有一些' - '
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key