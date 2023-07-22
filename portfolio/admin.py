from django.contrib import admin
from .models import Project, Experience, Education, Category

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)