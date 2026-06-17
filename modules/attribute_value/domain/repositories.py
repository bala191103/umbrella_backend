from abc import ABC, abstractmethod


class AttributeValueRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, guid):
        pass

    @abstractmethod
    def get_by_product(self, product_guid):
        pass