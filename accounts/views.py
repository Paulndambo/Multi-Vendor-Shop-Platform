from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
class UserListCreateAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    lookup_field = "pk"

    
class UserProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_superuser:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=user).all()

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            if instance.user == user:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Holah!, you can only update your profile"}, status=status.HTTP_400_BAD_REQUEST)