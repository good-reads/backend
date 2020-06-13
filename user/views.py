from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken

from .models import Account
from .serializers import (
    RegisterAccountSerializer,
    LoginUserSerializer,
    GetProfileSerializer,
    EditProfileSerializer,
    EditPasswordSerializer,
    AddMylistSerializer,
    SubMylistSerializer,
)


@api_view(['POST'])
def register_account(request):
    if request.method == 'POST':
        serializer = RegisterAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_account(request):
    if request.method == 'POST':
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)
        data = {
            'user_id': user.id,
            'token': token[1],
        }
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PATCH'])
@permission_classes([IsAuthenticated])
def get_or_update_account(request):
    account = get_object_or_404(Account, id=request.user.id)
    if request.method == 'GET':
        serializer = GetProfileSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = EditPasswordSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.save():
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        fields = request.data.keys()
        serializer = EditProfileSerializer(account, fields=fields, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def edit_my_list(request):
    if request.method == 'PATCH':
        account = get_object_or_404(Account, id=request.user.id)
        if request.data['type'] == 'ADD':
            serializer = AddMylistSerializer(account, data=request.data)
        else:
            serializer = SubMylistSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
