from django.urls import path
from .views import ProductListView, RetrieveProduct, ListPosts, PostDetails

urlpatterns = [
    path('api/v1/products', ProductListView.as_view(), name='product_list'),
    path('api/v1/products/<int:id>/', RetrieveProduct.as_view(), name='product_list'),

    path('api/v1/blog/post', ListPosts.as_view(), name='post_list'),
    path('api/v1/blog/post/<int:id>/', PostDetails.as_view(), name='post_details')
]
