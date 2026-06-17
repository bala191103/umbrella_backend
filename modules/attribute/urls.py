from django.urls import path

from modules.attribute.adapters.views import (
    AttributeCreateView,
    AttributeDetailView,
    CategoryAttributesView
)

urlpatterns = [

    path(
        "create/",
        AttributeCreateView.as_view()
    ),

    path(
        "<uuid:attribute_guid>/",
        AttributeDetailView.as_view()
    ),

    path(
        "category/<uuid:category_guid>/",
        CategoryAttributesView.as_view()
    )
]