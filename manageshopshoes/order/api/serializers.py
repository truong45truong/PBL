from order.models import Orders, Detail_orders
from product.models import Products
from rest_framework import serializers

class DetailOrderSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Detail_orders
        fields = ['product_id','status','quantity']
    def create(self, validated_data):
        print(validated_data)
        detail_order = Detail_orders.objects.create(**validated_data)
        return detail_order
class OrderSerializer(serializers.ModelSerializer):
    detailorders = DetailOrderSerializer(many=True)
    class Meta:
        model = Orders
        fields = [
            'name','datetime',
            'receiver','address_receiver',
            'phone_receiver','status',
            'total_price','customer_id',
            'transport_id','detailorders',
        ]