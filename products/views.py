from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

