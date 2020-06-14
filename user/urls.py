from django.urls import path

from .views import *

urlpatterns = [
    path("auth/register/", register_account),
    path("auth/login/", login_account),
    path("auth/account/get/", get_or_update_account),
    path("auth/account/update/", get_or_update_account),

    path("list/get/", get_or_create_list),
    path("list/create/", get_or_create_list),
    path("list/edit/", edit_list),
    path("list/delete/", delete_list),

    # path("review/write/", create_review),
]
