from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class ProductEntity:

    product_guid: UUID

    category_guid: UUID

    title: str

    description: str

    image: str | None

    price: float

    stock_quantity: int

    overall_rating: float

    views: int

    rating_count: int

    is_active: bool

    created_at: datetime | None = None

    updated_at: datetime | None = None