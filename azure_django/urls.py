from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_to_main),
    path('main/', views.main)
]