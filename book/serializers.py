from rest_framework import serializers

from config.serializers import DynamicFieldsModelSerializer
from .models import (
    Book, Review, Rate
)


class RegisterBookSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'intro', 'rate', 'thumbnail', 'img',)

    def create(self, validated_data):
        return Book.create(validated_data)

    def update(self, book, validated_data):
        book.title = validated_data.get('title', book.title)
        book.author = validated_data.get('author', book.author)
        book.intro = validated_data.get('intro', book.intro)
        book.rate = validated_data.get('rate', book.rate)
        book.thumbnail = validated_data.get('thumbnail', book.thumbnail)
        book.img = validated_data.get('img', book.img)
        book.save()
        return book


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only = ('id',)


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    rate_avg = serializers.FloatField(read_only=True)

    class Meta:
        model = Rate
        fields = '__all__'

    def create(self, validated_data):
        return Rate.create(validated_data)

    def update(self, rate, validated_data):
        return rate.update_score(validated_data)



class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'rate', 'thumbnail',)
