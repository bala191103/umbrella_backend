class GetCategoryAttributesUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        category_guid
    ):
        return self.repository.get_by_category(
            category_guid
        )