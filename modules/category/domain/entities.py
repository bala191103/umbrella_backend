from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class CategoryEntity:

    category_guid: UUID

    category_type_guid: UUID

    name: str

    description: str | None

    parent_category_guid: UUID | None

    created_at: datetime | None = None

    updated_at: datetime | None = None