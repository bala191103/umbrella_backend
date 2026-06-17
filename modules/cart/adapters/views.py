from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from modules.cart.adapters.serializers import CartSerializer
from modules.cart.adapters.repositories import DjangoCartRepository

from modules.cart.use_cases.add_to_cart import AddToCartUseCase
from modules.cart.use_cases.get_cart import GetCartUseCase
from modules.cart.use_cases.remove_from_cart import RemoveFromCartUseCase

# Create your views here.
class AddToCartView(APIView):

    def post(
        self,
        request
    ):

        serializer = CartSerializer(
            data=request.data
        )

        if serializer.is_valid():

            repository = (
                DjangoCartRepository()
            )

            use_case = (
                AddToCartUseCase(
                    repository
                )
            )

            cart = use_case.execute(
                serializer.validated_data
            )

            return Response(
                CartSerializer(cart).data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )
    
class UserCartView(APIView):

    def get(
        self,
        request,
        user_guid
    ):

        repository = (
            DjangoCartRepository()
        )

        use_case = (
            GetCartUseCase(
                repository
            )
        )

        cart_items = use_case.execute(
            user_guid
        )

        serializer = CartSerializer(
            cart_items,
            many=True
        )

        return Response(
            serializer.data
        )
    
class RemoveCartItemView(APIView):

    def delete(
        self,
        request,
        cart_guid
    ):

        repository = (
            DjangoCartRepository()
        )

        use_case = (
            RemoveFromCartUseCase(
                repository
            )
        )

        use_case.execute(
            cart_guid
        )

        return Response(
            status=204
        )