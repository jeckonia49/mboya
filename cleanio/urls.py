from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import (
    CleanioHomeView,
    ContactView,
    FAQView,
    PricingView,
)
from cleanio.utils.views import (
    subscribe_views
)

from django.contrib.sitemaps.views import sitemap
from .settings.sitemaps import (ArticleSitemap,StaticSitemap)

sitemaps = {
    'Article': ArticleSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CleanioHomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("order/", include("order.urls", namespace="order")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("faq/", FAQView.as_view(), name="faq"),
    path("pricing/", PricingView.as_view(), name="pricing"),
    path("subscribe/", subscribe_views, name="subscribe"),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# STATIC FILES PATH
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

# CUSTOM 404 AND 500 PAGES

def hander_404_view(request, exception):
    return render(request, "404.html", {})

handler404 = "cleanio.urls.hander_404_view"
# handler500 = ""
