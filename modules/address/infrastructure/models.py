from django.db import models
import uuid

from modules.users.infrastructure.models import User


class Address(models.Model):

    address_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    tag = models.CharField(
        max_length=20
    )

    full_address = models.TextField()

    city = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    pin_code = models.CharField(max_length=10)

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "address"