import datetime

from django.db import models
from django.shortcuts import get_list_or_404

from .rates import Rate


def upload_url(instance, filename):
    return 'book/covers/{0}/{1}'.format(instance.isbn, filename)

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30, unique=True)
    title = models.CharField(max_length=50, default="")
    author = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=512, default="")
    publisher = models.CharField(max_length=30, default="")
    pubdate = models.DateField()
    cover = models.ImageField(upload_to=upload_url)

    @property
    def rate(self):
        return Rate.objects.filter(book_isbn=self.isbn).aggregate(
            models.Avg('score')
        )['score__avg'] or 0

    class Meta:
        db_table = 'books'

    @classmethod
    def create(cls, params):
        return cls.objects.create(**params)

    @classmethod
    def get_popular_list(cls):
        params = {}
        return cls.objects.filter(**params)

    @classmethod
    def get_bestseller_list(cls):
        params = {}
        return cls.objects.filter(**params)

    @classmethod
    def search_books(cls, *args):
        condi = args[0]
        isbn = condi.get('isbn', None)
        if isbn:
            return cls.objects.filter(isbn=isbn)
        else:
            query_set = {
                'title__contains': condi.get('title', ''),
                'author__contains': condi.get('author', ''),
                'publisher__contains': condi.get('publisher', ''),
                'pubdate__range': (condi.get('start', datetime.datetime.min),
                                   condi.get('end', datetime.datetime.now()))
            }
            return cls.objects.filter(**query_set)

    # def update_rate(self, score):
    #     self.rate = score