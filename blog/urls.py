from django.urls import path
from .views import IndexView, BlogDetailView, AuthorView

app_name = 'blog'


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('story/<slug:slug>/',BlogDetailView.as_view(), name='blog-detail'),
    path('author/',AuthorView.as_view(), name='author'),
]