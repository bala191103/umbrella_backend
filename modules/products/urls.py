from django.urls import path

from modules.products.adapters.views import (
    ProductCreateView,
    ProductDetailView,
    ProductListView
)

urlpatterns = [

    path(
        "create/",
        ProductCreateView.as_view()
    ),

    path(
        "",
        ProductListView.as_view()
    ),

    path(
        "<uuid:product_guid>/",
        ProductDetailView.as_view()
    )
]