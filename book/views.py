from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from book.models import Book
from user.models import Account
from .serializers import (
    RegisterBookSerializer,
    BookDetailSerializer,
    BookListSerializer,
)


@api_view(['PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def register_or_update_book(request, **kwargs):
    fields = request.data.keys()

    if request.method == 'PUT':
        serializer = RegisterBookSerializer(fields=fields, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'PATCH':
        book = get_object_or_404(Book, id=kwargs['book_id'])
        serializer = RegisterBookSerializer(book, fields=fields, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'DELETE':
        book = get_object_or_404(Book, id=kwargs['book_id'])
        book.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_book_details(request):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=request.GET.get('book_id'))
        serializer = BookDetailSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_book_lists(request):
#     if request.method == 'GET':
#         data = {}
#
#         if request.GET.get('mylist', False):
#             user = get_object_or_404(Account, id=request.user.id)
#             data = GetMylistSerializer(user).data
#             data['mylist'] = BookListSerializer(
#                 data['mylist'],
#                 many=True,
#             ).data[:settings.BOOK_LIST_LIMITAION]
#
#         if request.GET.get('popular', False):
#             data['popular'] = BookListSerializer(
#                 Book.get_popular_list(),
#                 many=True,
#             ).data[:settings.BOOK_LIST_LIMITAION]
#
#         if request.GET.get('bestseller', False):
#             print(type(Book.get_bestseller_list()))
#             data['bestseller'] = BookListSerializer(
#                 Book.get_bestseller_list(),
#                 many=True,
#             ).data[:settings.BOOK_LIST_LIMITAION]
#
#         return Response(data, status=status.HTTP_200_OK)


