from celery import shared_task
from .models import Blog

@shared_task()
def add_like_to_blog_task(user, slug):
    blog = Blog.objects.get(slug=slug)
    if blog.likes.filter(id=user).exists():
        blog.likes.remove(user)
    else:
        blog.likes.add(user)