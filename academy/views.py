from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Course, CourseMaterials

class DashboardView(View):
    def get(self, request):
        categories = Category.objects.select_related()

        context = {
            'categories':categories
        }
        return render(request, 'academy/category.html', context)

class CategoryDetailView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        context = {
            'category':category
        }
        return render(request, 'academy/category-detail.html', context)
    
class CourseDetailView(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        context = {
            'course':course
        }
        return render(request, 'academy/course-detail.html', context)
    
    def post(self, request, slug):
        course = Course.objects.get(slug=slug)
        materials = CourseMaterials.objects.filter(playlist__slug=course.slug).first()
        course.students.add(request.user)
        course.save()
        return redirect('academy:learn-course',slug=slug, random_number=materials.random_number)

class CourseMaterialsView(View):
    def get(self, request, slug, random_number):
        course = Course.objects.get(slug=slug)
        if request.user in course.students.all():
            # filter_playlist = CourseMaterials.objects.filter(playlist__slug=course.slug).order_by('queue')
            # materials = filter_playlist.filter(random_number=random_number)
            materials = CourseMaterials.objects.filter(playlist__slug=course.slug, random_number=random_number)
            next_materials = CourseMaterials.objects.filter(playlist__slug=course.slug, random_number__gt=random_number).order_by('queue').first()
        else:
            return redirect('academy:course-detail',slug=slug)

        context = { 
            'course':course,
            'materials':materials,
            'next_materials':next_materials
        }
        return render(request, 'academy/course-materials.html', context)