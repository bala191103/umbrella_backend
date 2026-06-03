from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

from .repositories import DjangoUserRepository

from modules.users.use_cases.create_user import (
    CreateUserUseCase
)


class UserCreateView(APIView):

    def post(self, request):

        serializer = UserSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = DjangoUserRepository()

            use_case = CreateUserUseCase(
                repository
            )

            user = use_case.execute(
                serializer.validated_data
            )

            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )