
from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('search_action/', views.search_action, name='search_action'),
    path('transfer/', views.transfer, name='transfer'),
    path('transfer_action/', views.transfer_action, name='transfer_action'),
]
