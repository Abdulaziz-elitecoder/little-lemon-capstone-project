from rest_framework import serializers
from .models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Booking
        fields="__all__"    
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Menu
        fields = "__all__"