from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class ProfileSerializer(serializers.ModelSerializer):
    name = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'
        