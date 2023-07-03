from rest_framework import serializers
from product.models import *


class CategeoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'product_count')


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "description", "rating")


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rewiew
        fields = '__all__'
