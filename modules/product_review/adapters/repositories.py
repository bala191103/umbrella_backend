from modules.product_review.domain.repositories import (
    ProductReviewRepository
)

from modules.product_review.infrastructure.models import (
    ProductReview
)


class DjangoProductReviewRepository(
    ProductReviewRepository
):

    def create(self, data):

        return ProductReview.objects.create(
            **data
        )

    def get_by_id(self, review_guid):

        return ProductReview.objects.get(
            review_guid=review_guid
        )

    def get_by_product(
        self,
        product_guid
    ):

        return ProductReview.objects.filter(
            product_id=product_guid
        )