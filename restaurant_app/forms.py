# forms.py
from django import forms
from .models import Reservation, Membership, Items

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
    

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'time', 'number_of_people']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['reservation', 'reason']

