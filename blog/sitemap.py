from django.contrib.sitemaps import Sitemap
from .models import Blog, Category

class BlogSitemap(Sitemap):
    changefrq = 'daily'
    priority = 0.6
    protocol = 'http'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.added_date
    
    def location(self, obj):
        return '/blog/%s' % (obj.slug)
    
class CategorySitemap(Sitemap):
    changefrq = 'daily'
    priority = 0.6
    protocol = 'http'

    def items(self):
        return Category.objects.all()
    
    def location(self, obj):
        return '/blog/%s' % (obj.slug)
