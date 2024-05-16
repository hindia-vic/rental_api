from rest_framework import serializers
from django.contrib.auth.models import User
from . models import House

class HouseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=House
        fields=['id', 'address', 'size', 'type', 'price', 'sharing', 'text','author']


class UserSerializer(serializers.ModelSerializer):
    houses= serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'houses']
