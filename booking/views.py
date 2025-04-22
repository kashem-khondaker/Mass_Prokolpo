from django.shortcuts import render
from booking.models import Booking
from booking.serializers import BookingSerializer
from rest_framework import viewsets
from core.permissions import IsBookingActionAllowed
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsBookingActionAllowed]

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()

        if self.request.user.role == 'STUDENT':
            return self.queryset.select_related('user' , 'room').filter(user=self.request.user)
        return Booking.objects.select_related('user' , 'room')