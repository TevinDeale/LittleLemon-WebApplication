from .models import Menu, Booking
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    booking = Booking
    fields = ['name', 'no_of_guest', 'bookingDate']