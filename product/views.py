from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import *
from product.models import *
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategeoriesSerializers(categories, many=True)
        return Response(data.data)
    elif request.method == 'POST':
        serializers = CategeoriesSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def get_categories(request, id):
    categories = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        serializers = CategeoriesSerializers(categories)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializer = CategeoriesSerializers(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=200)


@api_view(['GET', 'POST'])
def list_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def get_products(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def list_review(request):
    if request.method == 'GET':
        review = Rewiew.objects.all()
        serializer = ReviewSerializers(review, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def get_review(request, id):
    review = get_object_or_404(Rewiew, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializers(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializers(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


