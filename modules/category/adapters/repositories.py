from modules.category.domain.repositories import (
    CategoryRepository
)

from modules.category.infrastructure.models import (
    Category
)


class DjangoCategoryRepository(
    CategoryRepository
):

    def create(self, data):

        return Category.objects.create(
            **data
        )

    def get_by_id(self, category_guid):

        return Category.objects.get(
            category_guid=category_guid
        )

    def get_all(self):

        return Category.objects.all()