from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        username_attr = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{username_attr: username})


USER_TYPES = (
    ("buyer", "Buyer"),
    ("seller", "Seller"),
)

STATUS_CHOICES = (
    ("active", "Active"),
    ("blocked", "Blocked"),
    ("inactive", "Inactive"),
)

class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    user_type = models.CharField(max_length=200, choices=USER_TYPES, default="buyer", null=True, blank=True)
    id_number = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=200, unique=True)
    postal_address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    current_location = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    

    objects = CustomUserManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initial_email = self.email

    def save(self, *args, **kwargs):
        if self.email != self._initial_email:
            self.email_confirmed = False
        super().save(*args, **kwargs)
