from django import forms
from .models import *
from django.forms import ModelForm

# Code style from -> https://www.geeksforgeeks.org/python-uploading-images-in-django/
class PetForm(forms.ModelForm):
    class Meta: 
        model = Pet 
        fields = ( 
                    'name', 'image', 'description','age',
                    'pet_type','breed','size', 'sex' ,'vaccinated',
                    'castrated','dewormed','vulnerable', 'isAdopted','adopted_by',
                 ) 
