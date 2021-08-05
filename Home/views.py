from django.shortcuts import render
from Dashboard.models import Posts


def home(request):
    posts = Posts.objects.all()
    return render(request, 'home.html', {'posts': posts});
