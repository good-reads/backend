from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("register/", BookAPI.as_view()),
    path("update/<int:book_id>/", BookAPI.as_view()),
    path("delete/<int:book_id>/", BookAPI.as_view()),
    path("get/", BookAPI.as_view()),
]
