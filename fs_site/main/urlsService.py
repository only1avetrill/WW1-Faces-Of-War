from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Main),
    path('main/', views.Main),
    path('index/', views.Main),
    path('auth/', views.Auth, name='auth'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('about/', views.About, name='about'),
]