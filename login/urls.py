from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
]
