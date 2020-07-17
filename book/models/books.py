from django.db import models

from .rates import Rate


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30, unique=True)
    title = models.CharField(max_length=50, default="")
    author = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=512, default="")
    publisher = models.CharField(max_length=30, default="")
    pubdate = models.DateField()
    cover = models.ImageField(
        upload_to=lambda instance, filename: 'book/covers/{0}/{1}'.format(instance.isbn, filename))

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

    # def update_rate(self, score):
    #     self.rate = score