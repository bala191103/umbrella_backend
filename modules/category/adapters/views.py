from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer
from .repositories import DjangoCategoryRepository

from modules.category.use_cases.create_category import (
    CreateCategoryUseCase
)

from modules.category.use_cases.get_category import (
    GetCategoryUseCase
)

from modules.category.use_cases.list_category import (
    ListCategoriesUseCase
)


class CategoryCreateView(APIView):

    def post(self, request):

        serializer = CategorySerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = (
                DjangoCategoryRepository()
            )

            use_case = (
                CreateCategoryUseCase(
                    repository
                )
            )

            category = (
                use_case.execute(
                    serializer.validated_data
                )
            )

            return Response(
                CategorySerializer(
                    category
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategoryDetailView(APIView):

    def get(
        self,
        request,
        category_guid
    ):

        repository = (
            DjangoCategoryRepository()
        )

        use_case = (
            GetCategoryUseCase(
                repository
            )
        )

        category = (
            use_case.execute(
                category_guid
            )
        )

        serializer = (
            CategorySerializer(
                category
            )
        )

        return Response(
            serializer.data
        )


class CategoryListView(APIView):

    def get(self, request):

        repository = (
            DjangoCategoryRepository()
        )

        use_case = (
            ListCategoriesUseCase(
                repository
            )
        )

        category = (
            use_case.execute()
        )

        serializer = (
            CategorySerializer(
                category,
                many=True
            )
        )

        return Response(
            serializer.data
        )