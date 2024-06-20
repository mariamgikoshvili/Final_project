from django import forms
from .models import Booking


class AvaliabilityForm(forms.Form):

    check_in = forms.DateField(required=True)
    check_out = forms.DateField(required=True)

