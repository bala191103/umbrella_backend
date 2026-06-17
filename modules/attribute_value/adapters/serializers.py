from rest_framework import serializers

from modules.attribute_value.infrastructure.models import (
    AttributeValue
)


class AttributeValueSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = AttributeValue

        fields = "__all__"