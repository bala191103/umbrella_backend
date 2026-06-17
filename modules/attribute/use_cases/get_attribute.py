class GetAttributeUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        attribute_guid
    ):
        return self.repository.get_by_id(
            attribute_guid
        )