from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
# Create your views here.
from api.models import Product, Post
from api.serializers import ProductSerializer, PostSerializer
from back_end.permissions import IsAuthorOrReadOnly


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ListPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
