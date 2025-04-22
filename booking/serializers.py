from rest_framework import serializers
from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Booking
        fields = ["user" , "room" , "check_in_date"  , "is_active" , "created_at"]
        read_only_fields = [ "is_active", "created_at"]