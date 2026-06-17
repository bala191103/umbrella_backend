from modules.cart.domain.repositories import (
    CartRepository
)

from modules.cart.infrastructure.models import (
    Cart
)


class DjangoCartRepository(
    CartRepository
):

    def add(self, data):

        return Cart.objects.create(
            **data
        )

    def get_user_cart(
        self,
        user_guid
    ):

        return Cart.objects.filter(
            user_id=user_guid
        )

    def remove(
        self,
        cart_guid
    ):

        cart = Cart.objects.get(
            cart_guid=cart_guid
        )

        cart.delete()