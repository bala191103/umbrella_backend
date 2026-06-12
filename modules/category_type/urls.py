from django.urls import path

from modules.category_type.adapters.views import (
    CategoryTypeCreateView,
    CategoryTypeDetailView,
    CategoryTypeListView
)

urlpatterns = [

    path(
        "create/",
        CategoryTypeCreateView.as_view()
    ),

    path(
        "",
        CategoryTypeListView.as_view()
    ),

    path(
        "<uuid:category_type_guid>/",
        CategoryTypeDetailView.as_view()
    )
]