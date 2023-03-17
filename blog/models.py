from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from .signals import add_gpt_response

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, null=True)
    body = RichTextField(blank=True)
    preview_image = models.FileField()
    category = models.ManyToManyField(Category, related_name='blogs')
    meta_description = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)
    estimated_read_time = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title
    
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