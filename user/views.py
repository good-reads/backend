from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import (
    UserSerializer, LoginSerializer, AccountSerializer, EditSerializer,
)
from .models import Account


def check_login(user):
    user = AuthToken.objects.get(user=user)
    if user:
        return user
    else:
        return None


@api_view(['POST'])
def register_account(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def update_account(request):
    if request.method == 'POST':
        account = get_object_or_404(Account, id=request.user.id)
        request.data['name'] = request.data.get('name', account.name)
        data = {
            'email': account.email,
            'name': account.name,
            'password': request.data['password']
        }
        serializer = AccountSerializer(account, data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.save():
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        account = get_object_or_404(Account, id=request.user.id)
        request.data['name'] = request.data.get('name', account.name)
        serializer = EditSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def login_account(request):
    if request.method == 'POST':
        print(AuthToken.objects.filter().count())
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = check_login(user)
        if not token:
            token = AuthToken.objects.create(user)
        data = {
            'user_id': user.id,
            'token': token[1],
        }
        return Response(data, status=status.HTTP_200_OK)


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

