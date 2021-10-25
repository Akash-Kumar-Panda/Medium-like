from django.conf.urls import url
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .forms import SignUpForm,BloggerDataForm 
from .models import BloggerData
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('list')

    else:
        form = SignUpForm()

    return render(request,'signup.html', {'form' : form, 'message': ''})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print(user)
            return redirect('list')

    else:
        form = AuthenticationForm()

    return render(request,'login.html', {'form' : form, 'message': ''})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('list')

def profile_view(request,user_id):

    if not BloggerData.objects.filter(pk = user_id).exists():
        message = "Blogger doesnot exist"
        return render(request,'errorPage.html',{'message' : message})

    blogger = User.objects.get(pk = user_id)
    bloggerData = BloggerData.objects.get(pk = user_id)

    return render(request,'profile.html',{'blogger': blogger, 'bloggerData' : bloggerData})

@login_required(login_url="/accounts/login/")
def register_as_blogger(request):

    user_id = request.user.id

    try:
        BloggerData.objects.get(pk = user_id)
        message = "Request already made"
        return render(request,'errorPage.html',{'message' : message})

    except:

        if request.method == 'POST':
            form = BloggerDataForm(data = request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = user_id
                data.save()

                # send_mail(
                #     'Blogger Access',
                #     'A new user ' +  request.user.first_name + ' ' + request.user.last_name + ' with user id ' + str(request.user.id) + ' has made a request for blogger access',
                #     'srijankhatri98@gmail.com',
                #     ['srijan.khatri@coriolis.co.in'],
                #     fail_silently=False,
                # )

                messages.success(request, 'Succesfully made blogger access request. The admin will be notified about your request.')
        else:
            form = BloggerDataForm()

    return render(request,'blogAccess.html',{'form':form, 'user_id': user_id})