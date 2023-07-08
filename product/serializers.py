from rest_framework import serializers
from product.models import *


class CategeoriesModelSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    class Meta:
        model = Category
        fields = ('name', 'product_count')


class ProductModelSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    class Meta:
        model = Product
        fields = ("title", "description", "rating")


class ReviewModelSerializers(serializers.ModelSerializer):
    text = serializers.CharField(max_length=100)
    class Meta:
        model = Rewiew
        fields = ['id', 'text', 'product', 'stars', 'product_id']
