from django.urls import path

from .views import *

urlpatterns = [
    path("auth/register/", register_account),
    path("auth/login/", login_account),
    path("auth/account/get/", get_or_update_account),
    path("auth/account/update/", get_or_update_account),

    path("auth/mylist/edit/", edit_my_list),
]
