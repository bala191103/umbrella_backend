from django.urls import path

from modules.attribute_value_type.adapters.views import (
    AttributeValueTypeCreateView,
    AttributeValueTypeDetailView,
    AttributeValueTypeListView
)

urlpatterns = [

    path(
        "create/",
        AttributeValueTypeCreateView.as_view()
    ),

    path(
        "",
        AttributeValueTypeListView.as_view()
    ),

    path(
        "<uuid:guid>/",
        AttributeValueTypeDetailView.as_view()
    ),
]