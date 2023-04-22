from django.urls import path
from .views import DashboardView

app_name = 'portfolio'

urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard')
]