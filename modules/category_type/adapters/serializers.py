from rest_framework import serializers

from modules.category_type.infrastructure.models import (
    CategoryType
)


class CategoryTypeSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = CategoryType

        fields = "__all__"