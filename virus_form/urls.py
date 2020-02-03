from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Outbreak-Form'),
    path('about/', views.about, name='Outbreak-About'),
]
