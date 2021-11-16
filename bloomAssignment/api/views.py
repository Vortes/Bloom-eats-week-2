from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Tweet
from .serializers import TweetSerializer, CreateUserSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def users(request):
    
    if request.method == "GET":
        users = User.objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        print("Hello " , request.data)
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def users_detail(request, pk):
    
    try:
        users = AppUser.objects.get(pk=pk)
    except AppUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(users)
        return Response(serializer.data)