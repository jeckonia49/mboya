from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user, login, logout
from django.http import HttpResponseRedirect
from order.forms import PickUpForm
from accounts.models import AccountUser, Profile
import random
import string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

def password_generator(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
    
    

class PickupOrderView(View):
    form_class = PickUpForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            email=form.cleaned_data.get("email")
            first_name=form.cleaned_data.get("full_name").split(" ")[0]
            user = AccountUser.objects.filter(email=email).first()
            instance = form.save(commit=False)
            if user is None:
                password=password_generator(10)
                user = AccountUser.objects.create_user(
                    email=email, 
                    password=password,
                    username=first_name
                    )
                instance.profile = Profile.objects.filter(user__email=user.email).first()
                instance.profile.full_name = form.cleaned_data.get("full_name")
                instance.save()
                form.save()
                protocol = "http"
                if request.is_secure():
                    protocol = "https"
                site_url = f"{protocol}://{get_current_site(request).domain}/"
                send_mail(
                    subject="ACCOUNT SETUP",
                    message=f"Hello {email}, we've noticed you dont have an account with us. We've created an account. Proceed to {site_url} to change your password. Your one time password is {password}",
                    recipient_list=[email],
                    from_email=settings.DEFAULT_FROM_EMAIL
                )
                
                send_mail(
                    subject="ORDER RECIVED",
                    message=f"Hello {email}, We've successfully received the pickup schedule and will get in touch with your soon. Thanks for choosing us.",
                    recipient_list=[email],
                    from_email=settings.DEFAULT_FROM_EMAIL
                )
                
            else:
                if request.user.is_authenticated:
                    instance.profile = request.user.user_profile
                instance.profile = Profile.objects.filter(user__email=user.email).first()
                instance.save()
                form.save()
                send_mail(
                    subject="ORDER RECIVED",
                    message=f"Hello {email}, We've successfully received the pickup schedule and will get in touch with your soon. Thanks for choosing us.",
                    recipient_list=[email],
                    from_email=settings.DEFAULT_FROM_EMAIL
                )
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

