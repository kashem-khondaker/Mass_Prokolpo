from django.urls import path , include
from rest_framework.routers import DefaultRouter
from booking.views import  BookingViewSet

router = DefaultRouter()

router.register('booking', BookingViewSet , basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/' , include('djoser.urls')),
    path('auth/' , include('djoser.urls.jwt')),
]