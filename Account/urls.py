from django.urls import path
from . import views

urlpatterns = [

    path('SignUp', views.sign_up, name="Sign Up"),
    path('Login', views.Login, name="Login")
]
