from django.contrib import admin

from .models import (
    Book, Review, Rate
)


class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'pubdate',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'content',)


class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book_isbn', 'score',)


admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rate, RateAdmin)
