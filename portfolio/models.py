from django.db import models
from cloudinary.models import CloudinaryField
import datetime

class Project(models.Model):
    name = models.CharField(max_length=200)
    about_project = models.TextField()
    link = models.URLField()
    preview_photo = CloudinaryField()
    views = models.IntegerField(default=0)

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