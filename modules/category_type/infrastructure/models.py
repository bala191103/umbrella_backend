

# Create your models here.
from django.db import models
import uuid


class CategoryType(models.Model):

    category_type_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category_type = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "category_type"