class GetAddressUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, address_guid):

        return self.repository.get_by_id(
            address_guid
        )