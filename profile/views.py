from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

from .forms import RegisterUserForm

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        else:
            form = RegisterUserForm

        context = {
            'form':form
        }

        return render(request, 'auth/register.html', context)
    
    def post(self, request):
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username=username, password=password)
            visit_count = request.session['visit_count']
            visit_count == 0
            login(request, user)
            return redirect('blog:index')
        else:
            return redirect('signup')  

class LoginView(View):
    def get(self, request):
        response = render(request, 'auth/login.html')
        if request.user.username in request.COOKIES:
            return redirect('blog:index')
        return response
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:index')
        else:
            return redirect('signin')
        
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('signin')