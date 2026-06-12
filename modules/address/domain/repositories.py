from abc import ABC, abstractmethod


class AddressRepository(ABC):

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_by_id(self, address_guid):
        pass