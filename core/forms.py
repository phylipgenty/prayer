from django import forms
from .models import Appointment, PrayerRequest

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'preferred_date', 'preferred_time', 'message']
        widgets = {
            'preferred_date': forms.Select(choices=[
                ('', 'Select preferred date'),
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
            ]),
            'preferred_time': forms.Select(choices=[
                ('', 'Select preferred time'),
                ('Morning (9am-12pm)', 'Morning (9am-12pm)'),
                ('Afternoon (1pm-4pm)', 'Afternoon (1pm-4pm)'),
                ('Evening (5pm-7pm)', 'Evening (5pm-7pm)'),
            ]),
        }

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['name', 'email', 'message']