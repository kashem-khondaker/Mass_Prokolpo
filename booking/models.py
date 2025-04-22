from django.db import models
from accounts.models import CustomUser
from mess.models import Room
# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'room')
    
    def __str__(self):
        return f"Booking by {self.user.username} for {self.room.room_number}"

