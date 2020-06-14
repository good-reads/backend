from django.contrib import admin

from book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',)


admin.site.register(Book, BookAdmin)
