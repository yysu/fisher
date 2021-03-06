from flask import current_app

from app.libs.httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    key_word_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        pass

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.key_word_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result


    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']