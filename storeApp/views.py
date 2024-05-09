from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer

# Create your views here.

@csrf_exempt
def productAPI(request, id=0):
    if request.method=='GET':
        product = Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    
    elif request.method=='POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Product Added Successfully", safe=False)
        return JsonResponse("Failed to add product", safe=False)
    
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(productId=product_data['productId'])
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated product successfully", safe=False)
        return JsonResponse("Failed to update product")
    
    elif request.method=='DELETE':
        product_data = JSONParser().parse(request)
        product=Product.objects.get(productId=product_data['productId'])
        product.delete()
        return JsonResponse("Deleted product successfully", safe=False)
    
        