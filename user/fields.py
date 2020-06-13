from rest_framework import serializers


class BookListingField(serializers.RelatedField):
    def to_representation(self, book):
        return {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'rate': book.rate,
            'thumbnail': book.thumbnail,
        }