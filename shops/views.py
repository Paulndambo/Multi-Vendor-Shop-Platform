from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import ShopSerializer, ItemImageSerializer, ItemSerializer
from .models import Shop, Item, ItemImage
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ShopListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser and user.is_staff:
            return Shop.objects.all()
        return Shop.objects.filter(owner=user).all()