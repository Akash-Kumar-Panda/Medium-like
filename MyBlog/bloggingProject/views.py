from django.shortcuts import render
from django.http import HttpResponse
from Blogs.models import Blog

def home(request):
    blogList = Blog.objects.all()
    return render(request,'home.html',{'blogList': blogList})