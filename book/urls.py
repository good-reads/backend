from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("register/", register_or_update_book),
    path("update/<int:book_id>/", register_or_update_book),
    path("delete/<int:book_id>/", register_or_update_book),

    path("get/details/", get_book_details),
    # path("get/lists/", get_book_lists),
]
