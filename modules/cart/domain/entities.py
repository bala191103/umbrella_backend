from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class CartEntity:

    cart_guid: UUID

    user_guid: UUID

    product_guid: UUID

    quantity: int

    created_at: datetime | None = None

    updated_at: datetime | None = None