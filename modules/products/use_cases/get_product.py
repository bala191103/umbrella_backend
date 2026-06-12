class GetProductUseCase:

    def __init__(self, repository):

        self.repository = repository

    def execute(self, product_guid):

        return self.repository.get_by_id(
            product_guid
        )