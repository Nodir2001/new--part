"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.post_list, name='post_list'),
]