from modules.attribute_value_type.domain.repositories import (
    AttributeValueTypeRepository
)

from modules.attribute_value_type.infrastructure.models import (
    AttributeValueType
)


class DjangoAttributeValueTypeRepository(
    AttributeValueTypeRepository
):

    def create(self, data):

        return AttributeValueType.objects.create(
            **data
        )

    def get_by_id(self, guid):

        return AttributeValueType.objects.get(
            attribute_value_type_guid=guid
        )

    def get_all(self):

        return AttributeValueType.objects.all()