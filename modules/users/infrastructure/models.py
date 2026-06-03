from django.db import models
import uuid

class User(models.Model):

    user_guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    full_name = models.CharField(max_length=150)

    dob = models.DateField()

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=15)

    insta_id = models.CharField(
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
        db_table = "user"