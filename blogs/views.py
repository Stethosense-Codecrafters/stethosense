from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def blog_post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post})

def About_us(request):
    return render(request,'centralapp/about_us.html')
def Cancer(request):
    return render(request,'centralapp/cancer.html')
def Covid_19(request):
    return render(request,'centralapp/Covid_19.html')
def Diabetes(request):
    return render(request,'centralapp/diabetes.html')
def FAQS(request):
    return render(request,'centralapp/faqs.html')
def Heart_disorder(request):
    return render(request,'centralapp/heart_disorder.html')
def doc_how_to_use(request):
    return render(request,'centralapp/how_to_use_Doctor.html')
def patients_how_to_use(request):
    return render(request,'centralapp/how_to_use_User.html')
def Hypertension(request):
    return render(request,'centralapp/hypertension.html')
def Inside_health_records(request):
    return render(request,'centralapp/inside_health_records.html')
def Aids(request):
    return render(request,'centralapp/aids.html')
