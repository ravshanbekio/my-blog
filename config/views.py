from django.shortcuts import render
from django.views import View

class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'privacy-policy.html')