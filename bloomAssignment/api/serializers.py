from rest_framework import serializers
from .models import AppUser, Tweet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'name', 'email', 'hobbies', 'favorite_food']


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'author', 'tweet_body', 'num_likes', 'num_retweets']