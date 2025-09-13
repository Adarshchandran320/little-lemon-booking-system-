from django.db import models
from django.utils import timezone

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    
    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')
    
    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} at {self.reservation_slot}:00"
