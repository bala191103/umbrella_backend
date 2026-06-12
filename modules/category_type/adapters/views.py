from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    CategoryTypeSerializer
)

from .repositories import (
    DjangoCategoryTypeRepository
)

from modules.category_type.use_cases.create_category_type import (
    CreateCategoryTypeUseCase
)

from modules.category_type.use_cases.get_category_type import (
    GetCategoryTypeUseCase
)

from modules.category_type.use_cases.list_category_type import (
    ListCategoryTypesUseCase
)

class CategoryTypeCreateView(
    APIView
):

    def post(self, request):

        serializer = CategoryTypeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = (
                DjangoCategoryTypeRepository()
            )

            use_case = (
                CreateCategoryTypeUseCase(
                    repository
                )
            )

            category_type = (
                use_case.execute(
                    serializer.validated_data
                )
            )

            return Response(
                CategoryTypeSerializer(
                    category_type
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CategoryTypeDetailView(
    APIView
):

    def get(
        self,
        request,
        category_type_guid
    ):

        repository = (
            DjangoCategoryTypeRepository()
        )

        use_case = (
            GetCategoryTypeUseCase(
                repository
            )
        )

        category_type = (
            use_case.execute(
                category_type_guid
            )
        )

        serializer = (
            CategoryTypeSerializer(
                category_type
            )
        )

        return Response(
            serializer.data
        )
    
class CategoryTypeListView(
    APIView
):

    def get(self, request):

        repository = (
            DjangoCategoryTypeRepository()
        )

        use_case = (
            ListCategoryTypesUseCase(
                repository
            )
        )

        category_types = (
            use_case.execute()
        )

        serializer = (
            CategoryTypeSerializer(
                category_types,
                many=True
            )
        )

        return Response(
            serializer.data
        )