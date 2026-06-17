from abc import ABC, abstractmethod


class CartRepository(ABC):

    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def get_user_cart(self, user_guid):
        pass

    @abstractmethod
    def remove(self, cart_guid):
        pass