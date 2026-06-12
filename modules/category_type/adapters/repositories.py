from modules.category_type.domain.repositories import (
    CategoryTypeRepository
)

from modules.category_type.infrastructure.models import (
    CategoryType
)


class DjangoCategoryTypeRepository(
    CategoryTypeRepository
):

    def create(self, data):

        return CategoryType.objects.create(
            **data
        )

    def get_by_id(
        self,
        category_type_guid
    ):

        return CategoryType.objects.get(
            category_type_guid=category_type_guid
        )

    def get_all(self):

        return CategoryType.objects.all()