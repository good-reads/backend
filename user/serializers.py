from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from user.models import Account, CustomList
from book.serializers import BookListSerializer
from config.serializers import DynamicFieldsModelSerializer


class RegisterAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'email', 'password',)

    def validate(self, data):
        validate_email(data['email'])
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        account = Account(**validated_data)
        account.set_password(validated_data['password'])
        account.save()
        return account


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class UserBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomList
        fields = ('id', 'owner_id', 'list_name',)

    def to_representation(self, custom_list):
        response = super().to_representation(custom_list)
        response['booklist'] = BookListSerializer(custom_list.booklist, many=True).data
        return response


class EditPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('password',)

    def validate(self, data):
        validate_password(data['password'])
        return data

    def update(self, account, validated_data):
        account.update_password(validated_data)
        return True


class ProfileSerializer(DynamicFieldsModelSerializer):
    booklist = UserBookListSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('name', 'email', 'booklist')


class AddListSerializer(UserBookListSerializer):
    class Meta:
        model = CustomList
        fields = ('id', 'booklist',)

    def update(self, custom_list, validated_data):
        book_list = validated_data.pop('booklist', [])
        for book in book_list:
            custom_list.booklist.add(book)
        return custom_list


class SubListSerializer(UserBookListSerializer):
    class Meta:
        model = CustomList
        fields = ('id', 'booklist',)

    def update(self, custom_list, validated_data):
        book_list = validated_data.pop('booklist', [])
        for book in book_list:
            custom_list.booklist.remove(book)
        return custom_list
