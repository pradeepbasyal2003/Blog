from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.

def Home(request):
    views = {}
    posts= Post.objects.all().order_by('-created_at')
    # views['post'] = posts
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')  
    views['page_obj'] = paginator.get_page(page_number)

    return render(request, "index.html", views)

def Post_view(request,slug):
    views={}
    post = Post.objects.get(slug = slug)
    views['post'] = post
    views['comments'] = Comment.objects.filter(post = post)
    return render(request,"post.html",views)

def add_comment(request,slug):
    pass