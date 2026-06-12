from django.db import models
import uuid

from modules.category_type.infrastructure.models import CategoryType


class Category(models.Model):

    category_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category_type = models.ForeignKey(
        CategoryType,
        on_delete=models.CASCADE,
        related_name="category"
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    parent_category = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "category"