from rest_framework import status
from rest_framework import response
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Tweet, UserContacts
from .serializers import TweetSerializer, CreateUserSerializer, UserContactsSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def users(request):
    
    if request.method == "GET":
        users = User.objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def users_detail(request, pk):
    
    try:
        users = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CreateUserSerializer(users)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreateUserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def tweets(request):
    if request.method == "GET":
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


@api_view(['POST', 'PUT', 'DELETE'])
def tweet_detail(request, pk):

    try:
        users = User.objects.get(pk=pk)
    except User.DoesNotExist:
        pass

    try:
        tweet_id = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        pass

    if request.method == "POST":
        serializer = TweetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=users)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = TweetSerializer(tweet_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tweet_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_contacts(request):
    if request.method == "GET":
        user_contacts = UserContacts.objects.all()
        serializer = UserContactsSerializer(user_contacts, many=True)
        return Response(serializer.data)


@api_view(['POST', 'PUT', 'DELETE'])
def user_contacts_detail(request, pk):

    try:
        users = User.objects.get(pk=pk)
    except User.DoesNotExist:
        pass

    try:
        user_contacts_id = UserContacts.objects.get(pk=pk)
    except UserContacts.DoesNotExist:
        pass

    if request.method == "POST":
        serializer = UserContactsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=users)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = UserContactsSerializer(user_contacts_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_contacts_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)