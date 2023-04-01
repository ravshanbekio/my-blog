from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogSitemap, CategorySitemap
from django.contrib.admin.sites import AdminSite
from django.shortcuts import redirect

# class MyAdminSite(AdminSite):

#     def check_admin(self, request):
#         if request.user == request.user.is_authenticated():
#             return redirect('manage/admin/')
#         else:
#             return redirect('index')

#     def get_urls(self):
#         urls = super().get_urls()
#         urls += [
#             path('manage/admin/', self.admin_view(self.check_admin))
#         ]
#         return urls

sitemaps = {
    'blog':BlogSitemap,
    'category':CategorySitemap
}

urlpatterns = [
    # path('manage/admin/',MyAdminSite.get_urls),
    path('manage/admin/',admin.site.urls),
    path('auth/',include('profile.urls')),
    path('accounts/', include('allauth.urls')),
    path('academy/',include('academy.urls')),
] + i18n_patterns(
    path('i18n/',include('django.conf.urls.i18n')),
    path('',include('blog.urls'), name=settings.LANGUAGES),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Ravshanbek Madaminov's Page AdminPanel"
admin.site.site_title = "Admin"
