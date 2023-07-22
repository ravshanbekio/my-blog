from django.shortcuts import render
from django.views import View

from .models import Project, Experience, Education, Category

class DashboardView(View):
    def get(self, request):
        categories = Category.objects.all()
        projects = Project.objects.select_related()[:6]
        experience = Experience.objects.all().order_by('-years')[:5]
        education = Education.objects.all().order_by('-years')[:5]

        context = {
            'categories':categories,
            'projects':projects,
            'experiences':experience,
            'educations':education
        }
        return render(request, 'portfolio/portfolio-masonry.html',context)
    
class ProjectDetailView(View):
    def get(self, request, pk):

        project = Project.objects.get(id=pk)
        project.views += 1
        project.save()
        context = {
            'project':project
        }

        return render(request, 'portfolio/portfolio-single-1.html', context)