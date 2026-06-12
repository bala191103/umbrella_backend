
from modules.products.domain.repositories import (
    ProductRepository
)

from modules.products.infrastructure.models import (
    Product
)


class DjangoProductRepository(
    ProductRepository
):

    def create(self, data):

        return Product.objects.create(
            **data
        )

    def get_by_id(self, product_guid):

        return Product.objects.get(
            product_guid=product_guid
        )

    def get_all(self):

        return Product.objects.all()