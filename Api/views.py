from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import House
from .serializers import HouseSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class Home(APIView):
    
    def get(self,request,format=None):
        houses = House.objects.all()
        serializer=HouseSerializer(houses,many=True)
        return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self,request,format=None):
        serializer=HouseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    def get_object(self,pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        house=self.get_object(pk)
        serializer=HouseSerializer(house)
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        house=self.get_object(pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk,format=None):
        house=self.get_object(pk)
        serializer=HouseSerializer(house,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer