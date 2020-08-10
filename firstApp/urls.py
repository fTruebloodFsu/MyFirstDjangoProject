from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='firstApp-home'),
    path('about/', views.about, name='firstApp-about'),
]