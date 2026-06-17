from rest_framework import serializers

from modules.product_review.infrastructure.models import (
    ProductReview
)


class ProductReviewSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = ProductReview
        fields = "__all__"