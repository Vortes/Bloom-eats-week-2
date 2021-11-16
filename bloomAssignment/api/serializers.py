from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['tweet_body', 'num_likes', 'num_retweets']