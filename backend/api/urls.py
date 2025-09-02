from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ping/<int:num>', views.ping),
    path('ping/', views.ping)
]