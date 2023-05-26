from celery import shared_task
from .models import Course

@shared_task()
def add_students_to_list_task(user,slug):
    course = Course.objects.get(slug=slug)
    course.students.add(user)
    course.save()
