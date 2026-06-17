from django.urls import path

from modules.attribute_value.adapters.views import (
    AttributeValueCreateView,
    AttributeValueDetailView,
    ProductAttributesView
)

urlpatterns = [

    path(
        "create/",
        AttributeValueCreateView.as_view()
    ),

    path(
        "<uuid:guid>/",
        AttributeValueDetailView.as_view()
    ),

    path(
        "product/<uuid:product_guid>/",
        ProductAttributesView.as_view()
    )
]