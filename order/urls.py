from django.urls import path
from .views import PickupOrderView


app_name = "order"
urlpatterns = [
    path("pickup/", PickupOrderView.as_view(), name="pickup-order"),
]
