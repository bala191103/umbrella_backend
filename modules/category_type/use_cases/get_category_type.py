class GetCategoryTypeUseCase:

    def __init__(self, repository):

        self.repository = repository

    def execute(
        self,
        category_type_guid
    ):

        return self.repository.get_by_id(
            category_type_guid
        )