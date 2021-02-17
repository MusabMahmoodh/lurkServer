from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
# Create your views here.
from .products import products


@api_view(['GET'])
def getRoutes(request):
    products = Product.objects.all()
    serielizer = ProductSerializer(products, many=True)
    return Response(serielizer.data)


@api_view(['GET'])
def getProducts(request):
    return Response(products)


@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    return Response(product)