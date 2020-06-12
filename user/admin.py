from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'date_joined',)
    filter_horizontal = ('mylist',)


admin.site.register(Account, AccountAdmin)
