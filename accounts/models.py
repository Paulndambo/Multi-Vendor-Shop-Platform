from django.db import models
from django.contrib.auth.models import User

USER_TYPES = (
    ("buyer", "Buyer"),
    ("seller", "Seller"),
)

STATUS_CHOICES = (
    ("active", "Active"),
    ("blocked", "Blocked"),
    ("inactive", "Inactive"),
)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=200, choices=USER_TYPES, default="buyer", null=True, blank=True)
    id_number = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=200, unique=True)
    postal_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    current_location = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="active")
    
    def __str__(self):
        return self.id_number