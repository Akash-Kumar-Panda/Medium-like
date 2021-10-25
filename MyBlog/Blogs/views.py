from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from Comments.models import Comment
from Accounts.models import BloggerData
from .models import Blog
from .forms import createBlogForm


def fetchBlog(request,blog_id):

    blogExists = Blog.objects.filter(pk =  blog_id).exists()

    if not blogExists :
        message = "Blog Doesnot Exist"
        return render(request,'errorPage.html',{'message' : message})

    blogDetail = Blog.objects.get(pk =  blog_id)
    blogOwner = User.objects.get(pk = blogDetail.user_id)
    comments = Comment.objects.filter(blog_id = blog_id)

    for item in comments:
        item.comOwner = User.objects.get(pk = item.user_id)

    request.session['blog_id'] = blog_id 
    request.session['blog_owner'] = blogOwner.id
    
    return render(request,'blog.html',{'blog': blogDetail,'blogOwner' : blogOwner, 'comments' : comments})

@login_required(login_url="/accounts/login/")
def updateBlog(request,blog_id=0):

    if not BloggerData.objects.filter(pk = request.user.id).exists() or BloggerData.objects.get(pk = request.user.id).status != 'verified':
        message = "You need a blogger acces to create a blog. Head over to the home page and request permission from the admin. Please wait for the admins action on your request if request already submitted"
        return render(request,'errorPage.html',{'message' : message})

    if request.method == 'POST':
        if blog_id:
            user = request.user.id
            currBlog = Blog.objects.get(pk=blog_id)
            blog_owner = currBlog.user_id

            if user != blog_owner:
                message = "Unauthorised access"
                return render(request,'errorPage.html',{'message' : message})

            form = createBlogForm(request.POST,request.FILES,instance=currBlog)

            if form.is_valid():
                form.save()

                messages.success(request, 'Blog Updated Succesfully!!')

        else:
            form = createBlogForm(request.POST,request.FILES)
            print(form)
            if form.is_valid():
                data = form.save(commit = False)
                data.user_id = request.user.id
                data.save()

                messages.success(request, 'Blog Created Succesfully!!')

    else:
        if blog_id:
            user = request.user.id
            currBlog = Blog.objects.get(pk=blog_id)
            blog_owner = currBlog.user_id

            if user != blog_owner:
                message = "Unauthorised access"
                return render(request,'errorPage.html',{'message' : message})

            form = createBlogForm(instance = currBlog)

        else:
            form = createBlogForm()

    return render(request,'update.html',{'form' : form, 'id' : blog_id})

@login_required(login_url="/accounts/login/")
def deleteBlog(request,blog_id):
    
    if request.user.id != Blog.objects.get(pk = blog_id).user_id:
        message = "Unauthorised access"
        return render(request,'errorPage.html',{'message' : message})
    else:
        Blog.objects.get(pk = blog_id).delete()
        messages.success(request, 'Blog Deleted Succesfully!!')

    return redirect('list')