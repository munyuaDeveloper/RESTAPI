from django.contrib import admin

# Register your models here.
from api.models import Product, Post

admin.site.register(Product)
admin.site.register(Post)
