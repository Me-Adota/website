from accounts.models import User
from django.db import models

class Pet(models.Model):
    PET_SIZES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    PET_SEX = [('M', 'Male'), ('F', 'Female')]

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pet_image', blank=True) 
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    birth_date = models.DateField()
    pet_type = models.CharField(max_length=10)
    breed = models.CharField(max_length = 50)
    size = models.CharField(max_length=1, choices=PET_SIZES)
    sex = models.CharField(max_length=1, choices=PET_SEX)
    vaccinated = models.BooleanField(default=False)
    castrated = models.BooleanField(default=False)
    dewormed = models.BooleanField(default=False)
    vulnerable = models.BooleanField(default=False)