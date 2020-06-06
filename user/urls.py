from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path("auth/account/<int:user_pk>/update/", AccountUpdateAPI.as_view()),
    path("auth/logout/", LoginAPI.as_view()),

    path("auth/<int:user_id>/add_list/", UserAPI.add_myList),
]
