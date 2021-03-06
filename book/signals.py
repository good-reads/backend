from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Book


@receiver(post_delete, sender=Book)
def remove_file_from_s3(sender, instance, **kwargs):
    instance.cover.delete(save=False)