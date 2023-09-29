from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def blog_post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post})

