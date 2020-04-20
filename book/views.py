from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import RegisterBookSerializer, BookSerializer


class RegisterBookAPI(generics.GenericAPIView):
    serializer_class = RegisterBookSerializer

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
