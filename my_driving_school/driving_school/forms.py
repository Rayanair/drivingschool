from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['instructor', 'student', 'date', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.TextInput(attrs={'type': 'text'})
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})


class PurchaseHoursForm(forms.Form):
    hours = forms.IntegerField(min_value=1, label='Nombre d\'heures à acheter')
