from django.shortcuts import render
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'PATCH'])
def profile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response({"error": "Profile data is not available"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        profile_serializer = ProfileSerializer(profile)
        return Response(profile_serializer.data)
    
    elif request.method == 'PATCH':
        profile_serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def profile_data(request):
    profiles = Profile.objects.all()[:1]
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)