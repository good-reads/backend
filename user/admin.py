from django.contrib import admin

from .models import (
    Account, CustomList,
)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'date_joined',)


class CustomListAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_name', 'owner_id',)
    filter_horizontal = ('booklist',)


admin.site.register(Account, AccountAdmin)
admin.site.register(CustomList, CustomListAdmin)
