from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modules.attribute_value.adapters.serializers import (
    AttributeValueSerializer
)

from modules.attribute_value.adapters.repositories import (
    DjangoAttributeValueRepository
)

from modules.attribute_value.use_cases.create_attribute_value import (
    CreateAttributeValueUseCase
)

from modules.attribute_value.use_cases.get_attribute_value import (
    GetAttributeValueUseCase
)

from modules.attribute_value.use_cases.get_product_attributes import (
    GetProductAttributesUseCase
)

class AttributeValueCreateView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = AttributeValueSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = (
                DjangoAttributeValueRepository()
            )

            use_case = (
                CreateAttributeValueUseCase(
                    repository
                )
            )

            attribute_value = (
                use_case.execute(
                    serializer.validated_data
                )
            )

            return Response(
                AttributeValueSerializer(
                    attribute_value
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class AttributeValueDetailView(
    APIView
):

    def get(
        self,
        request,
        guid
    ):

        repository = (
            DjangoAttributeValueRepository()
        )

        use_case = (
            GetAttributeValueUseCase(
                repository
            )
        )

        attribute_value = (
            use_case.execute(
                guid
            )
        )

        serializer = (
            AttributeValueSerializer(
                attribute_value
            )
        )

        return Response(
            serializer.data
        )
    
class ProductAttributesView(
    APIView
):

    def get(
        self,
        request,
        product_guid
    ):

        repository = (
            DjangoAttributeValueRepository()
        )

        use_case = (
            GetProductAttributesUseCase(
                repository
            )
        )

        values = (
            use_case.execute(
                product_guid
            )
        )

        serializer = (
            AttributeValueSerializer(
                values,
                many=True
            )
        )

        return Response(
            serializer.data
        )

