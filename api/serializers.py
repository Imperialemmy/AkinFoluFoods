from rest_framework import serializers
from users.models import CustomUser
from inventory.models import Brand, Category, Size, Ware, WareVariant, Batch, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone_number']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class WareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ware
        fields = '__all__'


class WareVariantSerializer(serializers.ModelSerializer):
    # ware = serializers.StringRelatedField()

    class Meta:
        model = WareVariant
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'