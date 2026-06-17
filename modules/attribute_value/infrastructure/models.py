from django.db import models

# Create your models here.
import uuid

from django.db import models

from modules.attribute.infrastructure.models import (
    Attribute
)

from modules.products.infrastructure.models import (
    Product
)


class AttributeValue(models.Model):

    attribute_value_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name="values"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="attribute_values"
    )

    value = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "attribute_value"
