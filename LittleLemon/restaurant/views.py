from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics , viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MenuItemsView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]