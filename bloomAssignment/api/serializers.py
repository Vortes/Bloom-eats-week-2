from rest_framework import serializers
from .models import AppUser, Tweet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['name', 'user_password', 'email']


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'tweet_body', 'num_likes', 'num_retweets']