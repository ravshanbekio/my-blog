from django.shortcuts import render
from django.views import View

from .models import Project, Experience, Education

class DashboardView(View):
    def get(self, request):
        projects = Project.objects.select_related()[:6]
        experience = Experience.objects.all().order_by('-years')[:5]
        education = Education.objects.all().order_by('-years')[:5]

        context = {
            'projects':projects,
            'experiences':experience,
            'educations':education
        }
        return render(request, 'portfolio/index.html',context)