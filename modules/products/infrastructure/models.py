from django.db import models

# Create your models here.

from django.db import models
import uuid

from modules.category.infrastructure.models import Category


class Product(models.Model):

    product_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    image = models.URLField(
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock_quantity = models.IntegerField(
        default=0
    )

    overall_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0
    )

    views = models.IntegerField(
        default=0
    )

    rating_count = models.IntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "product"