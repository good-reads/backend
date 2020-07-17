from rest_framework import serializers
from django.conf import settings

from config.serializers import DynamicFieldsModelSerializer
from .models import (
    Book, Review, Rate
)


class RegisterBookSerializer(DynamicFieldsModelSerializer):
    pubdate = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only = ('id',)


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rate = serializers.FloatField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    # rate_avg = serializers.FloatField(read_only=True)

    class Meta:
        model = Rate
        fields = '__all__'

    # def create(self, validated_data):
    #     return Rate.create(validated_data)

    # def update(self, rate, validated_data):
    #     return rate.update_score(validated_data)



class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'rate', 'cover',)
