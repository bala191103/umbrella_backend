from rest_framework import serializers

from modules.cart.infrastructure.models import (
    Cart
)


class CartSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Cart
        fields = "__all__"