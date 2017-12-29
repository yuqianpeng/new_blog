from django.shortcuts import render
from bog import  models
# Create your views here.
from django.db.models import Q
def list(request):
    blog = models.Blog.objects.all()
    context = {
        'blog':blog,
    }
    return render(request,'list.html',context)
def create(request):

    return render(request,'create.html')
def blog(request):
    keyword = request.GET.get('keyword','')

    if keyword is not None:
        blogs= models.Blog.objects.filter(title__icontains=keyword)
    else:
        blogs = models.Blog.objects.all()
    # blogs = models.Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request,'blog.html',context)

def Blogdetail(request,**kwargs):
    sid =int(kwargs['pk'])

    blog1s = models.Blog.objects.filter(pk=sid)

    context = {
        'blog1s':blog1s,
        'pk': sid,
    }
    return render(request,"detail.html",context)