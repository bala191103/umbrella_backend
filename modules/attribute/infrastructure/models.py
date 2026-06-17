from django.db import models

# Create your models here.
import uuid

from django.db import models

from modules.category.infrastructure.models import Category

from modules.attribute_value_type.infrastructure.models import (
    AttributeValueType
)


class Attribute(models.Model):

    attribute_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    parent_attribute = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="attributes"
    )

    title = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    value_type = models.ForeignKey(
        AttributeValueType,
        on_delete=models.PROTECT
    )

    options = models.JSONField(
        null=True,
        blank=True
    )

    icon_name = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "attribute"