from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from .serializers import BrandSerializer, CategorySerializer, SizeSerializer, WareSerializer, WareVariantSerializer, BatchSerializer, ImageSerializer
from inventory.models import Brand, Category, Size, Ware, WareVariant, Batch, Image
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from inventory.filters import WareFilter
from rest_framework.pagination import PageNumberPagination



class CustomVariantPagination(PageNumberPagination):
    page_size = 10  # Set to 10 items per page
    page_size_query_param = 'page_size'  # Optional: Allow overriding via ?page_size=X
    max_page_size = 100  # Optional: Cap for safety

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = WareFilter

class WareVariantViewSet(ModelViewSet):
    queryset = WareVariant.objects.all()
    serializer_class = WareVariantSerializer
    pagination_class = CustomVariantPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['ware__name']  # Search by ware name
    ordering_fields = ['last_updated']  # Order by last updated
    ordering = ['-last_updated']  # Default: last updated first

    def get_queryset(self):
        queryset = WareVariant.objects.all()
        # Annotate with the latest batch updated_at
        latest_batch = Batch.objects.filter(variant=OuterRef('pk')).order_by('-updated_at').values('updated_at')[:1]
        return queryset.annotate(last_updated=Subquery(latest_batch))

class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer