from django.db import models
from django.contrib.auth.models import User

from book.models import Book


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.CharField(max_length=500, blank=True)
    mylist = models.ManyToManyField(Book)
