from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'reservation_slot': forms.Select(attrs={'class': 'form-control'}, choices=[
                (10, '10:00 AM'),
                (11, '11:00 AM'),
                (12, '12:00 PM'),
                (13, '1:00 PM'),
                (14, '2:00 PM'),
                (15, '3:00 PM'),
                (16, '4:00 PM'),
                (17, '5:00 PM'),
                (18, '6:00 PM'),
                (19, '7:00 PM'),
                (20, '8:00 PM'),
            ])
        }
