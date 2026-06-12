from rest_framework import serializers

from modules.products.infrastructure.models import (
    Product
)


class ProductSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Product

        fields = "__all__"