from django import forms

from .models import Order, Contact, Subscription


class PickUpForm(forms.ModelForm):
    pickup_date = forms.CharField(widget=forms.TextInput(), required=False)
    delivery_date = forms.CharField(widget=forms.TextInput(), required=False)
    
    class Meta:
        model = Order
        fields = [
            'full_name', 
            "email",
            "phone", 
            "address", 
            "instructions", 
            "pickup_date", 
            "delivery_date"
            ]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your Full Names"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email address"}),
            "phone": forms.NumberInput(attrs={"placeholder": "Your active phone number"}),
            "address": forms.TextInput(attrs={"placeholder": "Your Address"}),
            "instructions": forms.Textarea(attrs={"placeholder": "Any instruction your might want us to know..."}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'phone', 'message']
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "example@gmail.com"}),
            "phone": forms.NumberInput(attrs={"placeholder": "07566353662"}),
            "message":forms.Textarea(attrs={"placeholder": "message..."})
        }

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email',]
        widgets = {"email": forms.EmailInput(attrs={"placeholder": "Enter your email address..."}),}



