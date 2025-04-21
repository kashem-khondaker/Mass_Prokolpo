from django.db import models
from accounts.models import CustomUser as User
from mess.models import Mess

# Create your models here.
class Expense(models.Model):
    EXPENSE_TYPES = (
        ('GROCERY', 'Grocery'),
        ('UTILITY', 'Utility (Electricity, Gas, Water)'),
        ('SERVICE', 'Service Charge'),
        ('OTHER', 'Other'),
    )
    
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=20, choices=EXPENSE_TYPES)
    description = models.TextField()
    date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_expense_type_display()} - {self.amount} - {self.date}"


class MealRecord(models.Model):
    MEAL_TYPES = (
        ('BREAKFAST', 'Breakfast'),
        ('LUNCH', 'Lunch'),
        ('DINNER', 'Dinner'),
    )
    
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE, related_name='meal_records')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals_taken')
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    date = models.DateField()
    is_taken = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('user', 'meal_type', 'date')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_meal_type_display()} - {self.date}"
