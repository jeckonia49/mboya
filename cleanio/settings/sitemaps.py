from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from order.models import Order

class ArticleSitemap(Sitemap):
    changefreq = "Always"
    priority = 1
    
    # def items(self):
    #     return Order.objects.all()
    
    # def location(self, obj):
    #     return reverse('order:detail', args=[obj.pk])
    
    # def lastmod(self, obj):
    #     return obj.updatedAt

class StaticSitemap(Sitemap):
    changefreq = 'Always'
    priority = 1
    
    # def items(self):
    #     return ['order']
    
    # def location(self, item):
    #     return reverse(item)