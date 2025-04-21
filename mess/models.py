from django.db import models
from accounts.models import CustomUser

class Mess(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=50)  # ঢাকা, চট্টগ্রাম ইত্যাদি
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    current_occupancy = models.PositiveIntegerField(default=0)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    rules = models.TextField()
    facilities = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Relations
    manager = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='managed_messes')
    monitors = models.ManyToManyField(CustomUser, related_name='monitored_messes')
    
    def __str__(self):
        return f"{self.name} - {self.city}"


class MessMember(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mess_memberships')
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE, related_name='members')
    joined_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('user', 'mess')
    
    def __str__(self):
        return f"{self.user.username} at {self.mess.name}"

class Room(models.Model):
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE , related_name='rooms')
    room_number = models.CharField(max_length=50)
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()

    def __str__(self):
        return f"{self.mess.name} - Room {self.room_number}"

class Review(models.Model):
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('mess', 'user')
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.mess.name}"

