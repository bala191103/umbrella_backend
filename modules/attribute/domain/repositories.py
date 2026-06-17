from abc import ABC, abstractmethod


class AttributeRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, attribute_guid):
        pass

    @abstractmethod
    def get_by_category(self, category_guid):
        pass