from django.urls import path
from . import views

urlpatterns = [

    path('NewPost', views.new_post, name="New Post"),
    path('Logout', views.logoutuser, name="Logout")
]