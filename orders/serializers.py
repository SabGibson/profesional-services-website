from rest_framework import serializers
from .models import Order,OrderItem
from products.serializers import ProductSerializer



class  MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity"
        )

class MyOrderSerializer(serializers.ModelSerializer):


    items = MyOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "postal_code",
            "country",
            "tel",
            "stripe_token",
            "items",
        ) 

class  OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = (

            "price",
            "product",
            "quantity"
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "postal_code",
            "country",
            "tel",
            "stripe_token",
            "items",
            "paid_value",
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order,**items_data)
        return order
    
