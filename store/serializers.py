from rest_framework import serializers
from .models import (
    Product, Order, OrderItem
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    unit_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    order = serializers.SerializerMethodField

    class Meta:
        model = OrderItem
        fields = "__all__"

    def get_name(self, obj):
        return obj.product.name
    
    def get_unit_price(self, obj):
        return obj.product.price

    def get_total_price(self, obj):
        total = obj.product.price * obj.quantity
        return total
    
    def get_order(self, obj):
        return obj.order