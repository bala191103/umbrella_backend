from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modules.products.adapters.serializers import (
    ProductSerializer
)

from modules.products.adapters.repositories import (
    DjangoProductRepository
)

from modules.products.use_cases.create_product import (
    CreateProductUseCase
)

from modules.products.use_cases.get_product import (
    GetProductUseCase
)

from modules.products.use_cases.list_products import (
    ListProductsUseCase
)

class ProductCreateView(APIView):

    def post(self, request):

        serializer = ProductSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = DjangoProductRepository()

            use_case = CreateProductUseCase(
                repository
            )

            product = use_case.execute(
                serializer.validated_data
            )

            return Response(
                ProductSerializer(product).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProductDetailView(APIView):

    def get(
        self,
        request,
        product_guid
    ):

        repository = DjangoProductRepository()

        use_case = GetProductUseCase(
            repository
        )

        product = use_case.execute(
            product_guid
        )

        serializer = ProductSerializer(
            product
        )

        return Response(
            serializer.data
        )
    
class ProductListView(APIView):

    def get(self, request):

        repository = DjangoProductRepository()

        use_case = ListProductsUseCase(
            repository
        )

        products = use_case.execute()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(
            serializer.data
        )