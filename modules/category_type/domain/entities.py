from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class CategoryTypeEntity:

    category_type_guid: UUID

    category_type: str

    description: str | None

    created_at: datetime | None = None

    updated_at: datetime | None = None