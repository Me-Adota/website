from django import forms
from .models import *
import requests
from django.forms import ModelForm


# Code style from -> https://www.geeksforgeeks.org/python-uploading-images-in-django/


class PetForm():
    # class Meta: 
    #     model = Pet 
    #     fields = [  'name', 'description','birth_date','pet_type','breed','size','sex','vaccinated','castrated','dewormed','vulnerable'] 

    name = forms.CharField(label='Nome', max_length=100)
    image = forms.FileField()
    description = forms.CharField(label='Descrição', max_length=100)
    birth_date = forms.DateField(label='Data de nascimento')
    pet_type = forms.CharField(label='Tipo do Pet', max_length=100)
    breed = forms.CharField(label='Raça', max_length=100)

    PET_SIZES = (('S', 'Small'), ('M', 'Medium'), ('L', 'Large'))
    size = forms.ChoiceField(choices=PET_SIZES)

    CHOICES = [('M','Masculino'),('F','Feminino')]
    sex=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))

    CHOICES = [('Y','Sim'),('N','Não')]
    vaccinated=forms.CharField(label='Vacinado', widget=forms.RadioSelect(choices=CHOICES))

    CHOICES = [('Y','Sim'),('N','Não')]
    castrated=forms.CharField(label='Castrado', widget=forms.RadioSelect(choices=CHOICES))

    CHOICES = [('Y','Sim'),('N','Não')]
    dewormed=forms.CharField(label='Domado', widget=forms.RadioSelect(choices=CHOICES))

    CHOICES = [('Y','Sim'),('N','Não')]
    vulnerable=forms.CharField(label='Vulneravel', widget=forms.RadioSelect(choices=CHOICES))

    CHOICES = [('Y','Sim'),('N','Não')]
    sex=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))

    # your_name = forms.CharField(label='Your name', max_length=100)
    # your_name = forms.CharField(label='Your name', max_length=100)
    # your_name = forms.CharField(label='Your name', max_length=100)
    # your_name = forms.CharField(label='Your name', max_length=100)
    