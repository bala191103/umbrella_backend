class GetCartUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        user_guid
    ):
        return self.repository.get_user_cart(
            user_guid
        )