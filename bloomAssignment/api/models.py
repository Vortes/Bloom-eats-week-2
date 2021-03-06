from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    tweet_body = models.CharField(max_length=280)
    num_likes = models.IntegerField()
    num_retweets = models.IntegerField()


class UserContacts(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
