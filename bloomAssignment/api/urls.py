from django.urls import path, include
from .views import users, users_detail

urlpatterns = [
    path('users/', users),
    path('user_detail/<int:pk>/', users_detail),
]