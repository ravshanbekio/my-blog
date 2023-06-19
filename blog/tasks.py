from celery import shared_task
from django.core.mail import send_mail
from .models import Blog

@shared_task()
def add_like_to_blog_task(user, slug):
    blog = Blog.objects.get(slug=slug)
    if blog.likes.filter(id=user).exists():
        blog.likes.remove(user)
    else:
        blog.likes.add(user)

@shared_task()
def send_email_task(title, text, sender, receiver):
    send_mail(title,
              text,
              sender,
              receiver)