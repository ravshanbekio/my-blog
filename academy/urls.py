from django.urls import path
from .views import AllCoursesView, CourseDetailView, CourseMaterialsView

app_name = 'academy'

urlpatterns = [
    path('',AllCoursesView.as_view(), name='dashboard'),
    path('course/<slug:slug>/',CourseDetailView.as_view(), name='course-detail'),
    path('course/<slug:slug>/<int:random_number>',CourseMaterialsView.as_view(), name='learn-course'),
]