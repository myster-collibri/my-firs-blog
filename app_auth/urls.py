from django.urls import path
from .views import*

urlpatterns=[
    path('',login_blog,name="login-blog"),
    path('register',register,name="register"),
    path('logout',logout_user,name="logout")
    ]