from django.contrib import admin

from django.contrib import admin
from .models import Tweet, UserContacts

# Register your models here.
admin.site.register(Tweet)
admin.site.register(UserContacts)