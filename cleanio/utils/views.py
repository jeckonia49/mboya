from order.forms import SubscriptionForm
from order.models import Subscription
from django.http import HttpResponseRedirect


def subscribe_views(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = Subscription.objects.update_or_create(**form.cleaned_data)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

