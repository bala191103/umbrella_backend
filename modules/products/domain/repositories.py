from abc import ABC, abstractmethod


class ProductRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, product_guid):
        pass

    @abstractmethod
    def get_all(self):
        pass