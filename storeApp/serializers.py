from rest_framework_mongoengine import serializers
from .models import Product, Customer

class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Product
        fields = ('productId', 'productName', 'productPrice')

class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Customer
        fields = ('customerName')