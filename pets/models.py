from users.models import User
from django.db import models

class Pet(models.Model):
    PET_SIZES = [('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')]
    PET_SEX = [('M', 'Macho'), ('F', 'Fêmea')]

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_image', blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    pet_type = models.CharField(max_length=10, blank=False, null=False)
    breed = models.CharField(max_length = 50, blank=False, null=False)
    size = models.CharField(max_length=1, choices=PET_SIZES, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=PET_SEX, blank=False, null=False)
    vaccinated = models.BooleanField(default=False)
    castrated = models.BooleanField(default=False)
    dewormed = models.BooleanField(default=False)
    vulnerable = models.BooleanField(default=False)
    isAdopted = models.BooleanField(default=False)
