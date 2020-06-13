from django.contrib import admin

from book.models.books import Book
from book.models.reviews import Review


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'content',)

admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)