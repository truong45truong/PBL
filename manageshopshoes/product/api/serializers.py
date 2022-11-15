from rest_framework.serializers import ModelSerializer
from product.models import Products, Prices, Sizes,Photo_products

class SizesSerializer(ModelSerializer):
    class Meta:
        model = Sizes
        fields = '__all__'
    def create(self, validated_data):
        size =Sizes.objects.create( **validated_data)
        return size
class PriceSerializer(ModelSerializer):
    class Meta:
        model = Prices
        fields = ['price','sale','datetime_create']
    def create(self, validated_data):
        price =Prices.objects.create( **validated_data)
        return price
class PhotoProductSerializer(ModelSerializer):
    class Meta:
        model = Photo_products
        fields = '__all__'
class ProductSerializer(ModelSerializer):
    prices = PriceSerializer(many=True)
    sizes = SizesSerializer(many=True)
    photo_products = PhotoProductSerializer(many=True)
    class Meta:
        model = Products
        fields = ['slug','name','sex','description','store_id','category_id','prices','sizes','photo_products']
    def create(self, validated_data):
        sizes=validated_data.pop('sizes')
        prices_data =validated_data.pop('prices')
        product= Products.objects.create(**validated_data)
        Prices.objects.create(product_id=product, **prices_data[0])
        for size in sizes:
            Sizes.objects.create(product_id=product,**size)
        return product
