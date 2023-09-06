from typing import Any, Dict
from django.views.generic import TemplateView, View
from order.forms import ContactForm


class CleanioHomeView(TemplateView):
    template_name = "index.html"

class ContactView(TemplateView):
    template_name = 'contact.html'
    form_class = ContactForm
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    


class FAQView(TemplateView):
    template_name = 'faq.html'


class PricingView(TemplateView):
    template_name = 'pricing.html'