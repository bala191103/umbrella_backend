from django.urls import path

from modules.category.adapters.views import (
    CategoryCreateView,
    CategoryDetailView,
    CategoryListView
)

urlpatterns = [

    path(
        "create/",
        CategoryCreateView.as_view()
    ),

    path(
        "",
        CategoryListView.as_view()
    ),

    path(
        "<uuid:category_guid>/",
        CategoryDetailView.as_view()
    )
]