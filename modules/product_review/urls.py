from django.urls import path

from modules.product_review.adapters.views import (
    ProductReviewCreateView,
    ProductReviewDetailView,
    ProductReviewListView
)

urlpatterns = [

    path(
        "create/",
        ProductReviewCreateView.as_view()
    ),

    path(
        "<uuid:review_guid>/",
        ProductReviewDetailView.as_view()
    ),

    path(
        "product/<uuid:product_guid>/",
        ProductReviewListView.as_view()
    )
]