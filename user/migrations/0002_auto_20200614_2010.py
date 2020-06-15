# Generated by Django 3.0.7 on 2020-06-14 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customlist',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_list', to=settings.AUTH_USER_MODEL),
        ),
    ]