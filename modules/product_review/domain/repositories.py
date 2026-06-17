from abc import ABC, abstractmethod


class ProductReviewRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, review_guid):
        pass

    @abstractmethod
    def get_by_product(self, product_guid):
        pass