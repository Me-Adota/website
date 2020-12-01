from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
from users.models import User

def All(request):
    if not request.user.is_authenticated:
        print("This is a not logged user bro:")
        return redirect('/accounts/login/')
    else:
        print("successfully logged")
    user = User.objects.all()
    return render(request, 'system/personal.html', {"user" : user})

def insertPets(request):

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user.id
            form.save()
            return redirect('/system/pets/my')
    else:
        form = PetForm()
    return render(request, 'system/insertpets.html', {'form' : form})

#get pets by logged user
def userPets(request):
    pets = Pet.objects.all()
    pets = pets.filter(user_id=request.user.id)
    print(pets)
    for pet in pets:
        print(pet.name)
    return render(request, 'system/myPetsRecords.html', {"pets" : pets})


def editPet(request,id):
    if not request.user.is_authenticated:
        print("This is a not logged user bro:")
        return redirect('/accounts/login/')
    else:
        print("successfully logged")
    pet = Pet.objects.get(id=id)
    form = PetForm(instance=pet)
    alert = {}
    if(pet.user_id != request.user.id):
        alert = {"info" : "Esse pet nao te pertence... Ainda."}
        alert = {"error" : "1"}

    if request.method == 'POST':
        form = PetForm(request.POST,request.FILES, instance=pet)
        form.save()
        return redirect('/system/pets/my' , flag='success')

    return render(request, 'system/editPet.html', {'pet':pet, 'alert':alert , 'form':form})

def petDelete(request, id):
    Pet.objects.filter(id=id).delete()
    return redirect('/system/pets/my')

def success(request):
    return HttpResponse('successfully uploaded')

