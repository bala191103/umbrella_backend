from abc import ABC, abstractmethod


class AttributeValueTypeRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, guid):
        pass

    @abstractmethod
    def get_all(self):
        pass