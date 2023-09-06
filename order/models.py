from typing import Any
from django.db import models
from accounts.models import Profile
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="order_profile")
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(help_text="0745547751")
    address = models.CharField(max_length=100)
    instructions = models.TextField(max_length=300, blank=True, null=True)
    completed = models.BooleanField(default=False)
    pickup_date = models.CharField(max_length=100, blank=True, null=True)
    delivery_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self) -> str:
        
        return self.full_name


class Contact(models.Model):
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.email

class Subscription(models.Model):
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email
    