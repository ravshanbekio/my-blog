from django.urls import path
from .views import DashboardView, ProjectDetailView

app_name = 'portfolio'

urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard'),
    path('<name>',ProjectDetailView.as_view(), name='project-detail'),
]