from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from book.models.books import Book


class UserManager(BaseUserManager):

    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.update({
            'is_admin': True,
            'is_staff': True,
            'is_superuser': True,
        })
        return self._create_user(email, password, **kwargs)


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20, null=False, unique=True)
    mylist = models.ManyToManyField(Book)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'accounts'
        ordering = ('id',)
