from rest_framework.serializers import ModelSerializer
from product.models import Products, Categories, Prices, Sizes


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'