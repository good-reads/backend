from django.contrib.auth.models import User
from django.db.models.signals import (
    post_save, post_delete
)
from django.dispatch import receiver

from user.models.accounts import Account


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()


@receiver(post_delete, sender=Account)
def remove_thumbnail_from_s3(sender, instance, **kwargs):
    instance.thumbnail.delete(save=False)