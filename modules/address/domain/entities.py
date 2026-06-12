from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AddressEntity:

    address_guid: UUID

    user_guid: UUID

    tag: str

    full_address: str

    city: str

    district: str

    state: str

    pin_code: str

    latitude: float | None

    longitude: float | None

    created_at: datetime | None = None

    updated_at: datetime | None = None