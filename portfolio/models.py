from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name

class Project(models.Model):
    name = models.CharField(max_length=200)
    about_project = RichTextField()
    link = models.URLField()
    preview_photo = CloudinaryField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    company_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=30)
    description = models.TextField(max_length=300, blank=True)
    location = models.URLField(blank=True)
    years = models.DateField(auto_now_add=False)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.company_name}-{self.years}"
    
class Education(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.URLField(blank=True)
    description = models.TextField(max_length=100)
    years = models.DateField(auto_now_add=False)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.company_name