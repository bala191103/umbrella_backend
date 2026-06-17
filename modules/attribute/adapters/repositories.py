from modules.attribute.domain.repositories import (
    AttributeRepository
)

from modules.attribute.infrastructure.models import (
    Attribute
)


class DjangoAttributeRepository(
    AttributeRepository
):

    def create(self, data):

        return Attribute.objects.create(
            **data
        )

    def get_by_id(
        self,
        attribute_guid
    ):

        return Attribute.objects.get(
            attribute_guid=attribute_guid
        )

    def get_by_category(
        self,
        category_guid
    ):

        return Attribute.objects.filter(
            category_id=category_guid
        )