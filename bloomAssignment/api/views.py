from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
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


@csrf_exempt
def users_detail(request, pk):
    
    try:
        users = AppUser.objects.get(pk=pk)
    except AppUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UserSerializer(users)
        return JsonResponse(serializer.data)