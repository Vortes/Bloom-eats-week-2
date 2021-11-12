from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import AppUser, Tweet
from .serializers import UserSerializer, TweetSerializer

@csrf_exempt
def users(request):
    
    if request.method == "GET":
        users = AppUser.objects.all()
        print(users)
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)