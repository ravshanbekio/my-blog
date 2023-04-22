from django.urls import path
from .views import DashboardView, CategoryDetailView, CourseDetailView, CourseMaterialsView

app_name = 'academy'

urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard'),
    path('filter=<slug:slug>/',CategoryDetailView.as_view(), name='category'),
    path('course/<slug:slug>/',CourseDetailView.as_view(), name='course-detail'),
    path('course/<slug:slug>/<int:random_number>',CourseMaterialsView.as_view(), name='learn-course'),
]