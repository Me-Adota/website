from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
from users.models import User
# from django.core.urlresolvers import reverse

# Create your views here.
def All(request):
    if not request.user.is_authenticated:
        print("This is a not logged user bro:")
        return redirect('/accounts/login/')
    else:
        print("successfully logged")
    user = User.objects.all()
    return render(request, 'system/personal.html', {"user" : user})

def insertPets(request):
    if not request.user.is_authenticated:
        return render(request, '')
    u = User.objects.get(id=request.user.id)
    
    if request.method == 'POST':
        # form = PetForm()
        # PetForm.objects.create(image = 'image.jpg',name = 'name', description= 'description', birth_date ='birth_date', pet_type = 'pet_type', breed = 'breed',size = 'S', sex = 'M', vaccinated ='vaccinated', castrated = 'castrated', dewormed = 'dewormed',vulnerable ='vulnerable')
        pets = (Pet)
        form = pets.objects.create(
            user_id = request.user.id,
            # image = FILE['image'],
            name = request.POST['name'],
            description = request.POST['description'],
            birth_date = request.POST['birth_date'],
            pet_type = request.POST['pet_type'] ,
            breed = request.POST['breed'] ,
            size = request.POST['size'],
            sex = request.POST['sex'],
            vaccinated = request.POST['vaccinated'],
            castrated = request.POST['castrated'],
            dewormed = request.POST['dewormed'],
            vulnerable = request.POST['vulnerable']
        )
    else:
        form = PetForm()
    return render(request, 'system/insertpets.html' , {'form': form})

#get pets by logged user
def userPets(request):
    pets = Pet.objects.all()
    pets = pets.filter(user_id=request.user.id)
    
    print(pets)
    for pet in pets:
        print(pet.name)


    return render(request, 'system/myPetsRecords.html', {"pets" : pets})

def success(request): 
    return HttpResponse('successfully uploaded') 