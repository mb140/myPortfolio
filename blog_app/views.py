from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # bring newest 5 blogs
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog_app/blogshomev1.html', {'blogs':blogs}  )
#   , {'blogs':blogs}