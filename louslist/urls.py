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
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('<str:department>', views.DepartmentView.as_view(), name='department'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.logout_user, name='logout'),
    #path('login', include('main.urls')),

]