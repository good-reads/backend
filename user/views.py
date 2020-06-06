from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken

from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, AccountSerializer
from .models import Account


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)
        print(token[0])
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token[1],
            }
        )

    def delete(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated]
        token = get_object_or_404(AuthToken, user=request.data['user_id'])
        token.delete()
        return Response(
            {
                "logout": "success"
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def add_myList(self, request, *args, **kwargs):
        instance = get_object_or_404(Account, user=kwargs['user_id'])
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        return Response(
            {
                "add_myList": request.data['books']
            }
        )


class AccountUpdateAPI(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = "user_pk"
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
