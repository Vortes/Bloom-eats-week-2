from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    hobbies = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    tweet_body = models.CharField(max_length=280)
    num_likes = models.IntegerField
    num_retweets = models.IntegerField
