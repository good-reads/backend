from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken

from user.models import Account, CustomList
from .serializers import (
    RegisterAccountSerializer,
    LoginUserSerializer,
    ProfileSerializer,
    EditPasswordSerializer,
    UserBookListSerializer,
    AddListSerializer,
    SubListSerializer,
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
        serializer = ProfileSerializer(account)
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
        serializer = ProfileSerializer(account, fields=fields, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def get_or_create_list(request):
    if request.method == 'GET':
        custom_list = get_list_or_404(CustomList, owner_id=request.user.id)
        serializer = UserBookListSerializer(custom_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        request.data['owner_id'] = request.user.id
        serializer = UserBookListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_list(request):
    if request.method == 'DELETE':
        custom_list = get_object_or_404(CustomList, id=request.data['list_id'])
        custom_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_list(request):
    if request.method == 'PUT':
        custom_list = get_object_or_404(CustomList, id=request.data['list_id'])
        print(request.data)
        if request.data['type'] == 'ADD':
            serializer = AddListSerializer(custom_list, data=request.data)
        else:
            serializer = SubListSerializer(custom_list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def create_review(request):
#     if request.method == 'PUT':
#