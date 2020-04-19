from rest_framework import serializers

from .models import Book


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author")

    def create(self, validated_data):
        book = Book.objects.create(
            title=validated_data['title'], author=validated_data['author'])
        return book
