from django.shortcuts import get_object_or_404
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class Backend(BaseBackend):
    def authenticate(self, data, **kwargs):
        try:
            """
            user login first
            """
            email = data.get('email', None)
            password = data.get('password', None)

            user = get_object_or_404(User, email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except AttributeError:
            pass
