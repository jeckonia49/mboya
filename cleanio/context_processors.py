from django.conf import settings
from order.forms import PickUpForm
from order.forms import SubscriptionForm
from accounts.auth.forms import (
    LoginForm,
)
def cleanio_site_context(request):
    return dict(
        telephone_contact=settings.SITE_CONTACT_TELEPHONE,
        email_contact=settings.DEFAULT_FROM_EMAIL,
        pickup_form_class=PickUpForm(),
        subscription_form=SubscriptionForm(),
        login_form=LoginForm(),
    )