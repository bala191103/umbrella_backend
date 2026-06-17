from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    ProductReviewSerializer
)

from .repositories import (
    DjangoProductReviewRepository
)

from modules.product_review.use_cases.create_review import (
    CreateReviewUseCase
)

from modules.product_review.use_cases.get_review import (
    GetReviewUseCase
)

from modules.product_review.use_cases.get_product_review import (
    GetProductReviewsUseCase
)

class ProductReviewCreateView(
    APIView
):

    def post(
        self,
        request
    ):

        serializer = ProductReviewSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = (
                DjangoProductReviewRepository()
            )

            use_case = (
                CreateReviewUseCase(
                    repository
                )
            )

            review = use_case.execute(
                serializer.validated_data
            )

            return Response(
                ProductReviewSerializer(
                    review
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProductReviewDetailView(
    APIView
):

    def get(
        self,
        request,
        review_guid
    ):

        repository = (
            DjangoProductReviewRepository()
        )

        use_case = (
            GetReviewUseCase(
                repository
            )
        )

        review = use_case.execute(
            review_guid
        )

        serializer = (
            ProductReviewSerializer(
                review
            )
        )

        return Response(
            serializer.data
        )
    
class ProductReviewListView(
    APIView
):

    def get(
        self,
        request,
        product_guid
    ):

        repository = (
            DjangoProductReviewRepository()
        )

        use_case = (
            GetProductReviewsUseCase(
                repository
            )
        )

        reviews = use_case.execute(
            product_guid
        )

        serializer = (
            ProductReviewSerializer(
                reviews,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    
