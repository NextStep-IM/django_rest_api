from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ping/', views.ping),
    path('ping/<int:num>', views.ping),
]