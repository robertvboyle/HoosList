from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'louslist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('login', include('main.urls')),
]