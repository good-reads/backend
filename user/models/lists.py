from django.db import models

from book.models import Book
from .accounts import Account


class CustomList(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(Account, related_name='booklist', on_delete=models.CASCADE)
    list_name = models.CharField(max_length=20, default="커스텀 리스트")
    booklist = models.ManyToManyField(Book)

    class Meta:
        db_table = 'custom_list'

    @classmethod
    def create(cls, params):
        return cls.objects.create(**params)