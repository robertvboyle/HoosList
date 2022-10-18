from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'louslist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('', include('main.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    
    #path('', include('main.urls')),
    #path('login', include('main.urls')),   
]