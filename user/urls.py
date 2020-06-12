from django.urls import path

from .views import *

urlpatterns = [
    path("auth/register/", register_account),
    path("auth/login/", login_account),
    path("auth/user/", UserAPI.as_view()),
    path("auth/account/update/", update_account),

    path("auth/<int:user_id>/add_list/", UserAPI.add_myList),
]
