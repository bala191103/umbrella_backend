from abc import ABC, abstractmethod


class CategoryTypeRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, category_type_guid):
        pass

    @abstractmethod
    def get_all(self):
        pass