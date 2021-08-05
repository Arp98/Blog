from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.contrib import messages


@login_required(login_url='/Account/Login')
def new_post(request):
    if request.method == 'POST':
        Post_User = request.user.get_username()
        Post_name = request.POST['Post_name']
        Post_Tags = request.POST['Post_Tags']
        Post_Contents = request.POST['Post_Content']

        Posts.objects.create(Post_User=Post_User, Post_name=Post_name, Post_Tags=Post_Tags, Post_Contents=Post_Contents)

        messages.success(request, 'Post Successfully Saved')
        return redirect('/Dashboard/NewPost')

    else:
        return render(request, 'New_Post.html')


@login_required(login_url='/Account/Login')
def logoutuser(request):
    logout(request)
    return redirect('/Account/Login')
