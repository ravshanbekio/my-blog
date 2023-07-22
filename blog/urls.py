from django.urls import path
from .views import IndexView, BlogDetailView, AddCommentView

app_name = 'blog'


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<slug:slug>/',AddCommentView.as_view(), name='add-comment'),
]