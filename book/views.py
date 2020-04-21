from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book


class RegisterBookAPI(generics.GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response(
            {
                "book": BookSerializer(
                    book, context=self.get_serializer_context()
                ).data
            }
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(
            Book, id=request.data.get('id'))
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response(
            {
                "book": BookSerializer(
                    book, context=self.get_serializer_context()
                ).data
            }
        )
