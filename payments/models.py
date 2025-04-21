from django.db import models
from accounts.models import CustomUser as User
from mess.models import Mess

# Create your models here.

class Payment(models.Model):
    PAYMENT_TYPES = (
        ('ADVANCE', 'Advance Payment'),
        ('MONTHLY', 'Monthly Fee'),
        ('EXTRA', 'Extra Payment'),
        ('REFUND', 'Refund'),
    )
    
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES)
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_date = models.DateField()
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='received_payments')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.payment_date}"

