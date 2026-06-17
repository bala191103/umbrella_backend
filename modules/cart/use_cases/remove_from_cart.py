class RemoveFromCartUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        cart_guid
    ):
        self.repository.remove(
            cart_guid
        )