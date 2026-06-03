class GetUserUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_guid):
        return self.repository.get_by_id(
            user_guid
        )