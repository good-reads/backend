from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book


class BookAPI(generics.GenericAPIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(**request.data)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response(BookSerializer(
            book, context=self.get_serializer_context()).data)

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Book, id=kwargs['book_id'])
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response(BookSerializer(
            book, context=self.get_serializer_context()).data)

    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs['book_id'])
        book.delete()
        return Response(BookSerializer(
            book, context=self.get_serializer_context()).data)
