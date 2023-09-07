from django.conf import settings
from order.forms import PickUpForm
from order.forms import SubscriptionForm
from django.contrib.sites.shortcuts import get_current_site
from accounts.auth.forms import (
    LoginForm,
)
def cleanio_site_context(request):
    protocol = "http"
    if request.is_secure():
            protocol = "https"
    site_base_url = f"{protocol}://{get_current_site(request).domain}"
    return dict(
        telephone_contact=settings.SITE_CONTACT_TELEPHONE,
        email_contact=settings.DEFAULT_FROM_EMAIL,
        pickup_form_class=PickUpForm(),
        subscription_form=SubscriptionForm(),
        login_form=LoginForm(),
        site_base_url=site_base_url,
    )