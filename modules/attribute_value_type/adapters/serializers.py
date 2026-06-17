from rest_framework import serializers

from modules.attribute_value_type.infrastructure.models import (
    AttributeValueType
)


class AttributeValueTypeSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = AttributeValueType

        fields = "__all__"