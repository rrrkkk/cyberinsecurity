
from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]
