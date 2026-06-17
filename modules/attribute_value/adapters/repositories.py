from modules.attribute_value.domain.repositories import (
    AttributeValueRepository
)

from modules.attribute_value.infrastructure.models import (
    AttributeValue
)


class DjangoAttributeValueRepository(
    AttributeValueRepository
):

    def create(self, data):

        return AttributeValue.objects.create(
            **data
        )

    def get_by_id(self, guid):

        return AttributeValue.objects.get(
            attribute_value_guid=guid
        )

    def get_by_product(
        self,
        product_guid
    ):

        return AttributeValue.objects.filter(
            product_id=product_guid
        )