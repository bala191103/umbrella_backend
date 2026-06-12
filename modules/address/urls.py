from django.urls import path

from modules.address.adapters.views import (
    AddressCreateView
)

urlpatterns = [
    path(
        "create/",
        AddressCreateView.as_view()
    )
]