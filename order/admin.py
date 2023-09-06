from django.contrib import admin
from .models import Order, Contact, Subscription

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["profile",'full_name', "email", "phone", "address", "completed", "pickup_date", "delivery_date"]
    list_display_links = ['full_name', "email", "phone", "address",]
    list_filter = ['profile', 'completed']
    search_fields = ['profile', 'email', 'address']

    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp']