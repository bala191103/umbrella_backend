from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AttributeEntity:

    attribute_guid: UUID

    category_guid: UUID

    value_type_guid: UUID

    title: str

    description: str

    options: dict | None

    icon_name: str | None

    created_at: datetime | None = None

    updated_at: datetime | None = None