from django.db import models

from .books import Book
from user.models import Account


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    content = models.CharField(max_length=512)

    class Meta:
        db_table = 'reviews'

    @classmethod
    def create(cls, data):
        return cls.objects.create(**data)
