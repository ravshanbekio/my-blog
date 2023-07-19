from django.shortcuts import render, redirect
from django.views import View
from .models import Course, CourseMaterials
from .tasks import add_students_to_list_task


class AllCoursesView(View):
    def get(self, request):
        courses = Course.objects.select_related()
        context = {
            'courses':courses
        }
        return render(request, 'academy/category-detail.html', context)
    
class CourseDetailView(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        materials = CourseMaterials.objects.filter(playlist__slug=course.slug).first()
        if request.user in course.students.all():
            return redirect('academy:learn-course',slug=course.slug, random_number=materials.random_number)
        context = {
            'course':course,
        }
        return render(request, 'academy/course-detail.html', context)
    
    def post(self, request, slug):
        course = Course.objects.get(slug=slug)
        materials = CourseMaterials.objects.filter(playlist__slug=course.slug).first()
        add_students_to_list_task.delay(
            user=request.user.id, slug=slug
        )
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
    
class MarkGraduatesView(View):
    def get(self, request, course_slug):
        course = Course.objects.get(slug=course_slug)
        course.graduates.add(request.user)  
        course.save()
        return redirect('academy:dashboard')