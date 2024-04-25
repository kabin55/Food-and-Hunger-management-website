"""
URL configuration for p1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from a1 import views

admin.site.site_header = "Food and Hungery Management System - Admin Panel"
admin.site.site_title = "Admin Portal for FH management website"
admin.site.index_title = "Welcome to FH management website"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.index,name="index"),
    path("",views.home,name="home"),
    #path("/",views.home,name="home"),
    path("login/",views.login, name="login"),
    path("signup/",views.signup, name="signup"),
    path("aboutus/",views.aboutus,name="about"),
    path("contact/",views.contact,name="contact"),
    
    path("information/",views.information,name="infromation"),

    path('donate/', views.donate, name='donate'),
    path('success/', views.donate_success, name='donate_success'),
    # path("donate/",views.donate ,name="donate"),
    
    
    
]
