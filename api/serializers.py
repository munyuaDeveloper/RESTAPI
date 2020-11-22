from rest_framework import serializers

from api.models import Product, Post


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'quantity', 'price']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'image', 'created']
