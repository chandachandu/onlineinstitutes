"""schoolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from admin import views
from django.views.generic import TemplateView



urlpatterns = [
    path('student/', include("student.urls")),
    path('faculty/', include("faculty.urls")),
    path('', TemplateView.as_view(template_name="main.html"), name="index"),
    path('login/', views.showLogin, name="login"),
    path('validate/', views.verifylogin, name="verify"),
    path('admin/', views.showadmindashboard, name="admin"),
    path('admins/', views.showadmins, name="admins"),
    path('create/', views.addadmin, name="addadmin"),
    path('courses/', views.viewCourses, name="courses"),
    path('addcourse/', views.addCourses, name="addCourse"),
    path('classes/',views.classeslist,name="classes"),
    path('schedule/', views.scheduleform, name="schedule"),
    path('logout', views.Deletesession, name="logout"),
]
