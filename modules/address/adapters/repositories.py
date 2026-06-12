from modules.address.domain.repositories import (
    AddressRepository
)

from modules.address.infrastructure.models import (
    Address
)


class DjangoAddressRepository(AddressRepository):

    def create(self, data):

        return Address.objects.create(**data)

    def get_by_id(self, address_guid):

        return Address.objects.get(
            address_guid=address_guid
        )

    def get_by_user(self, user_guid):

        return Address.objects.filter(
            user_id=user_guid
        )