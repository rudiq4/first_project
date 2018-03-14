from django import forms
from .models import Vehicle
from django.shortcuts import render_to_response


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        #fields =['marka', 'model']
        exclude = ["flag"]


