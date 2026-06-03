from modules.users.domain.repositories import UserRepository
from modules.users.infrastructure.models import User


class DjangoUserRepository(UserRepository):

    def create(self, data):
        return User.objects.create(**data)

    def get_by_id(self, user_guid):
        return User.objects.get(
            user_guid=user_guid
        )