from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AttributeValueTypeEntity:

    attribute_value_type_guid: UUID

    name: str

    created_at: datetime | None = None

    updated_at: datetime | None = None