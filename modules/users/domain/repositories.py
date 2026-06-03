from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, user_guid):
        pass