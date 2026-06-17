from django.urls import path

from modules.cart.adapters.views import (
    AddToCartView,
    UserCartView,
    RemoveCartItemView
)

urlpatterns = [

    path(
        "add/",
        AddToCartView.as_view()
    ),

    path(
        "user/<uuid:user_guid>/",
        UserCartView.as_view()
    ),

    path(
        "<uuid:cart_guid>/",
        RemoveCartItemView.as_view()
    )
]