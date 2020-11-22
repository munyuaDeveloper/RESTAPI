from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post-image')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
