from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import *
from product.models import *
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategeoriesSerializers(categories, many=True)
        return Response(data.data)


@api_view(['GET'])
def get_categories(request, id):
    categories = get_object_or_404(Category, id=id)
    serializers = CategeoriesSerializers(categories)
    return Response(serializers.data)


@api_view(['GET'])
def list_products(request):
    if request.method == "GET":
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_products(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)

@api_view(['GET'])
def list_review(request):
    if request.method == 'GET':
        review = Rewiew.objects.all()
        serializer = ReviewSerializers(review, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_review(request, id):
    review = get_object_or_404(Rewiew, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializers(review)
        return Response(serializer.data)

# Create your views here.
