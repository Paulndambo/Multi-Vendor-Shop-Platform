from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subscription(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    products_limit = models.IntegerField(default=1)

    def __str(self):
        return self.title

STATUS_CHOICES = (
    ("active", "Active"),
    ("deactivated", "Deactivated"),
    ("suspended", "Suspended"),
)

class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    description = models.TextField()
    dominant_products = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    location = models.JSONField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='active', choices=STATUS_CHOICES)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    subscription_status = models.CharField(max_length=255, default='active', choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="item_images")
    stock = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="item_images")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name
