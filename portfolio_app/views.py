from django.shortcuts import render
from .models import Project

def homev1(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home_v1.html', {'projects':projects} )