from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AttributeValueEntity:

    attribute_value_guid: UUID

    attribute_guid: UUID

    product_guid: UUID

    value: str

    created_at: datetime | None = None

    updated_at: datetime | None = None