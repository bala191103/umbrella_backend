class GetAttributeValueTypeUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        guid
    ):
        return self.repository.get_by_id(
            guid
        )