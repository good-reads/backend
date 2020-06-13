from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from .models import Account
from .fields import BookListingField
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

class EditPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('password',)

    def validate(self, data):
        validate_password(data['password'])
        return data

    def update(self, account, validated_data):
        account.set_password(validated_data['password'])
        account.save()
        return True


class GetProfileSerializer(serializers.ModelSerializer):
    mylist = BookListingField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('name', 'email', 'mylist',)


class EditProfileSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'email',)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AddMylistSerializer(serializers.ModelSerializer):
    mylist = BookListingField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('mylist',)

    def update(self, account, validated_data):
        for book in validated_data['mylist']:
            account.mylist.add(book)
        return account


class SubMylistSerializer(serializers.ModelSerializer):
    mylist = BookListingField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('mylist',)

    def update(self, account, validated_data):
        for book in validated_data['mylist']:
            account.mylist.remove(book)
        return account


class GetMylistSerializer(serializers.ModelSerializer):
    mylist = BookListingField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('mylist',)
