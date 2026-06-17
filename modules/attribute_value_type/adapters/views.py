from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modules.attribute_value_type.adapters.serializers import (
    AttributeValueTypeSerializer
)

from modules.attribute_value_type.adapters.repositories import (
    DjangoAttributeValueTypeRepository
)

from modules.attribute_value_type.use_cases.create_attribute_value_type import (
    CreateAttributeValueTypeUseCase
)

from modules.attribute_value_type.use_cases.get_attribute_value_type import (
    GetAttributeValueTypeUseCase
)

from modules.attribute_value_type.use_cases.get_all_attribute_value_types import (
    GetAllAttributeValueTypesUseCase
)
class AttributeValueTypeCreateView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = (
            AttributeValueTypeSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            repository = (
                DjangoAttributeValueTypeRepository()
            )

            use_case = (
                CreateAttributeValueTypeUseCase(
                    repository
                )
            )

            attribute_value_type = (
                use_case.execute(
                    serializer.validated_data
                )
            )

            return Response(
                AttributeValueTypeSerializer(
                    attribute_value_type
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class AttributeValueTypeDetailView(
    APIView
):

    def get(
        self,
        request,
        guid
    ):

        repository = (
            DjangoAttributeValueTypeRepository()
        )

        use_case = (
            GetAttributeValueTypeUseCase(
                repository
            )
        )

        attribute_value_type = (
            use_case.execute(
                guid
            )
        )

        serializer = (
            AttributeValueTypeSerializer(
                attribute_value_type
            )
        )

        return Response(
            serializer.data
        )
    
class AttributeValueTypeListView(
    APIView
):

    def get(
        self,
        request
    ):

        repository = (
            DjangoAttributeValueTypeRepository()
        )

        use_case = (
            GetAllAttributeValueTypesUseCase(
                repository
            )
        )

        items = (
            use_case.execute()
        )

        serializer = (
            AttributeValueTypeSerializer(
                items,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    
