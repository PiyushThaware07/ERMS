"""ERMS_Projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('emp_register',views.emp_register,name="emp_register"),
    path('emp_login',views.emp_login,name="emp_login"),
    # Interface
    path('emp_Interface',views.emp_Interface,name="emp_Interface"),
    path('emp_changePassword',views.emp_changePassword,name="emp_changePassword"),
    path('emp_logout',views.emp_logout,name="emp_logout"),
    path('emp_profile',views.emp_profile,name="emp_profile"),
    path('emp_education',views.emp_education,name="emp_education"),
    path('edit_Education',views.edit_Education,name="edit_Education"),
]
