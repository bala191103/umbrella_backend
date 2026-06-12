from abc import ABC, abstractmethod


class CategoryRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, category_guid):
        pass

    @abstractmethod
    def get_all(self):
        pass