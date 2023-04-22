from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage
from .signals import add_gpt_response
import re

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, max_length=200)
    body = RichTextField(blank=True)
    preview_image = CloudinaryField()
    category = models.ManyToManyField(Category, related_name='blogs')
    meta_description = models.CharField(max_length=160)
    meta_keyword = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='post_likes')
    added_date = models.DateField(auto_now_add=True)
    estimated_read_time = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Blog,self).save(*args, **kwargs)

        self.preview_image = CloudinaryImage(str(self.preview_image)).image(height=200, width=150, crop="lfill")
        print(self.preview_image)
    
    def number_of_likes(self):
        return self.likes.count()
    
@receiver(post_save, sender=Category)
def post_save_category(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()
    
@receiver(post_save, sender=Blog)
def pre_save_blog(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()

add_gpt_response(instance=Blog)