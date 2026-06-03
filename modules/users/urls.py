from django.urls import path

from modules.users.adapters.views import (
    UserCreateView
)

urlpatterns = [
    path(
        "create/",
        UserCreateView.as_view()
    )
]