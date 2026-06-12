from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AddressSerializer

from .repositories import DjangoAddressRepository

from modules.address.use_cases.create_address import (
    CreateAddressUseCase
)


class AddressCreateView(APIView):

    def post(self, request):

        serializer = AddressSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = DjangoAddressRepository()

            use_case = CreateAddressUseCase(
                repository
            )

            address = use_case.execute(
                serializer.validated_data
            )

            return Response(
                AddressSerializer(address).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
