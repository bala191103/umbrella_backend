class GetReviewUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        review_guid
    ):
        return self.repository.get_by_id(
            review_guid
        )