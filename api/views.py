from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from .serializers import BrandSerializer, CategorySerializer, SizeSerializer, WareSerializer, WareVariantSerializer, BatchSerializer, ImageSerializer
from inventory.models import Brand, Category, Size, Ware, WareVariant, Batch, Image
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser





class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class WareViewSet(ModelViewSet):
    queryset = Ware.objects.all()
    serializer_class = WareSerializer

class WareVariantViewSet(ModelViewSet):
    queryset = WareVariant.objects.all()
    serializer_class = WareVariantSerializer

class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer