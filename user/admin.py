from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_pk', 'email']
    filter_horizontal = ('mylist',)


admin.site.register(Account, AccountAdmin)
