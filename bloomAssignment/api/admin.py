from django.contrib import admin

from django.contrib import admin
from .models import AppUser, Tweet

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Tweet)