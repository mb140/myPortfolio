from django.shortcuts import render,get_object_or_404
from .models import Blog

def all_blogs(request):
    # bring newest 5 blogs
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog_app/blogshomev1.html', {'blogs':blogs}  )
#   , {'blogs':blogs}

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog_app/detail.html',{'blog':blog})