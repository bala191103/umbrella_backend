from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class ProductReviewEntity:

    review_guid: UUID

    product_guid: UUID

    user_guid: UUID

    rating: int

    description: str

    image: str | None

    created_at: datetime | None = None

    updated_at: datetime | None = None