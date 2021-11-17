from django.urls import path, include
from .views import tweets, user_contacts, user_contacts_detail, users, users_detail, tweet_detail

urlpatterns = [
    path('users/', users),
    path('user_detail/<int:pk>/', users_detail),
    path('tweets/', tweets),
    path('tweet_detail/<int:pk>/', tweet_detail),
    path('user_contacts/', user_contacts),
    path('user_contacts_detail/<int:pk>/', user_contacts_detail),
]