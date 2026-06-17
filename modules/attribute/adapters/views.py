from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modules.attribute.adapters.serializers import (
    AttributeSerializer
)

from modules.attribute.adapters.repositories import (
    DjangoAttributeRepository
)

from modules.attribute.use_cases.create_attribute import (
    CreateAttributeUseCase
)

from modules.attribute.use_cases.get_attribute import (
    GetAttributeUseCase
)

from modules.attribute.use_cases.get_category_attribute import (
    GetCategoryAttributesUseCase
)

class AttributeCreateView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = AttributeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = (
                DjangoAttributeRepository()
            )

            use_case = (
                CreateAttributeUseCase(
                    repository
                )
            )

            attribute = use_case.execute(
                serializer.validated_data
            )

            return Response(
                AttributeSerializer(
                    attribute
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class AttributeDetailView(
    APIView
):

    def get(
        self,
        request,
        attribute_guid
    ):

        repository = (
            DjangoAttributeRepository()
        )

        use_case = (
            GetAttributeUseCase(
                repository
            )
        )

        attribute = (
            use_case.execute(
                attribute_guid
            )
        )

        serializer = (
            AttributeSerializer(
                attribute
            )
        )

        return Response(
            serializer.data
        )
    
class CategoryAttributesView(
    APIView
):

    def get(
        self,
        request,
        category_guid
    ):

        repository = (
            DjangoAttributeRepository()
        )

        use_case = (
            GetCategoryAttributesUseCase(
                repository
            )
        )

        attributes = (
            use_case.execute(
                category_guid
            )
        )

        serializer = (
            AttributeSerializer(
                attributes,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    
    