from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # blogs = Project.objects.all()
    return render(request, 'blog_app/blogshomev1.html' )
#   , {'blogs':blogs}