from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ["id", 'name']




class UserGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff']

class UserPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']





class ItemGETSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = models.Item
        fields = ['id', 'name', 'location', 'model', 'quantity', 'description', 'tags']

class ItemPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['id', 'name', 'location', 'model', 'quantity', 'description', 'tags']






class CartItemGETSerializer(serializers.ModelSerializer):
    item = ItemGETSerializer(read_only=True, many=False)
    owner = UserGETSerializer(read_only=True, many=False)
    class Meta:
        model = models.CartItem
        fields = ['id', 'item', 'owner', 'quantity']

class CartItemPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ['id', 'item', 'owner', 'quantity']





class RequestGETSerializer(serializers.ModelSerializer):
    requester = UserGETSerializer(read_only=True, many=False)
    item      = ItemGETSerializer(read_only=True, many=False)
    class Meta:
        model = models.Request
        fields = ['id', 'requester', 'item', 'quantity', 'date_open', 'open_reason', 'status']

class RequestPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        fields = ['id', 'requester', 'item', 'quantity', 'date_open', 'open_reason']
