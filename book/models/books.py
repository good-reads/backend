from django.db import models
from django.conf import settings


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    intro = models.CharField(max_length=512)
    rate = models.FloatField(default=0)

    thumbnail = models.URLField(default=settings.IMG_BASE_URL)
    img = models.URLField(default=settings.IMG_BASE_URL)

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

    def update_rate(self, score):
        self.rate = score