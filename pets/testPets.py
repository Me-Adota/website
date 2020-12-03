from .models import Pet
from django.test import TestCase
from users.models import UserManager, User
from pets import views 
from urllib import request
class InsertionTestCase(TestCase):
    #Insertion test test
    @classmethod

    def setUpTestData(cls):
        User.objects.create(full_name="Joao", email="test@gmail.com",  password="sadasda165a1d6a8sd496c1a6c1x65c1ad")
        Pet.objects.create(name="pet name value 1", user_id = 1  ,description = "asxcz zxczxcqd",age = 32,
            pet_type = "CACHORRO",breed = "Akita",size = "M", sex = "F" ,vaccinated = False,
            castrated = True ,dewormed = True,vulnerable = True, isAdopted = True)

        Pet.objects.create(name="pet name value 2", user_id = 1  ,description = "Description of second pet",age = 12,
            pet_type = "CACHORRO",breed = "Akita",size = "S", sex = "M" ,vaccinated = True,
            castrated = True ,dewormed = True,vulnerable = True, isAdopted = True)
        pass

    def test_get_pet_success_name(self):
        user = User.objects.get(pk=1)
        dog = Pet.objects.get(name="pet name value 1")
        user.save()
        dog.save()
        
        self.assertEqual(user.full_name, 'Joao')
        self.assertEqual(dog.name, "pet name value 1")
        
    def test_user_change_pets_status(self):
        user = User.objects.get(pk=1)
        dog = Pet.objects.get(name="pet name value 1")
        user.save()
        dog.save()
        dog.isAdopted = True
        dog.save()
        self.assertEqual(dog.isAdopted, True)
    
    def test_check_change(self):
        user = User.objects.get(pk=1)
        dog = Pet.objects.get(name="pet name value 1")
        user.save()
        dog.save()
        self.assertEqual(dog.isAdopted, True)
