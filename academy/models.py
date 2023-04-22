from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, blank=True)
    photo = CloudinaryField()

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name
    
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_relation')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_owner')
    main_title = models.CharField(max_length=200)
    about_course = models.TextField(max_length=800)
    photo = CloudinaryField()
    students = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Playlist Courses"
        
    def __str__(self):
            return self.main_title
    
class CourseMaterials(models.Model):
    playlist = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    video = CloudinaryField(blank=True)
    link = models.URLField(blank=True)
    queue = models.IntegerField(default=0)
    random_number = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Course materials"

    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=Category)
def add_category_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()

@receiver(pre_save, sender=Course)
def add_course_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.main_title)
        instance.save()

@receiver(pre_save, sender=CourseMaterials)
def random_course_number(instance, *args, **kwargs):
    if instance.random_number == 0:
        instance.random_number = random.randint(100000, 999999)
        instance.save()