from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import createCommentForm

# Create your views here.
@login_required(login_url="/accounts/login/")
def update_comment(request,com_id = 0):

    blog_id = request.session['blog_id']
    blog_owner = request.session['blog_owner']

    if request.method == 'POST':
        if com_id:
            user = request.user.id
            currCom = Comment.objects.get(pk=com_id)
            comment_owner = currCom.user_id

            if user != blog_owner and user != comment_owner:
                message = "Unauthorised access"
                return render(request,'errorPage.html',{'message' : message})

            form = createCommentForm(request.POST,instance=currCom)

            if form.is_valid():
                form.save()

                messages.success(request, 'Comment Updated Succesfully!!')
                return redirect('list')

        else:
            form = createCommentForm(request.POST)

            if form.is_valid():
                data = form.save(commit = False)
                data.user_id = request.user.id
                data.blog_id = blog_id
                data.save()

                messages.success(request, 'Comment Created Succesfully!!')
                return redirect('list')

    else:
        if com_id:
            user = request.user.id
            currCom = Comment.objects.get(pk=com_id)
            comment_owner = currCom.user_id

            if user != comment_owner and user != blog_owner:
                message = "Unauthorised access"
                return render(request,'errorPage.html',{'message' : message})

            form = createCommentForm(instance = currCom)

        else:
            form = createCommentForm()

    return render(request,'update.html',{'form' : form, 'id' : com_id})


@login_required(login_url="/accounts/login/")
def delete_comment(request,comment_id):

    blog_owner = request.session['blog_owner']
    
    if request.user.id != Comment.objects.get(pk = comment_id).user_id and request.user.id != blog_owner:
        message = "Unauthorised access"
        return render(request,'errorPage.html',{'message' : message})
    else:
        Comment.objects.get(pk = comment_id).delete()
        messages.success(request, 'Comment Deleted Succesfully!!')

    return redirect('list')