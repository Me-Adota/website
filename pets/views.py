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
    user = User.objects.get(pk=request.user.id)
    user.save()

    error = {}
    errors = { 'has_errors' : 0 } 
        
    if(user.cpf == '' or user.full_name == '' or user.mobile_phone == '' or user.zip_code == ''):
        errors = { 'has_errors' : 1 } 
        errors['error'] = {}
        errors['error'].update({ 0 : 'Antes de cadastrar um pet para adoção é necessário que você complete seu cadastro com telefone, cpf, nome e CEP!'})

    if request.method == 'POST' and errors['has_errors'] == 0: 
        form = PetForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.instance.user_id = request.user.id
            form.save() 
            return redirect('/system/pets/my')
    elif(request.method == 'POST' and errors['has_errors'] == 1):
        errors['error'].update({ 0 : 'Complete seu cadastro!'})
    else:
        form = PetForm() 
    return render(request, 'system/insertpets.html', {'form' : form , 'errors' : errors}) 

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

    errors = {}
    errors = { 'has_errors' : 0 } 
    errors['error'] = {}

    if(pet.user_id != request.user.id):
        errors['has_errors'] = 1
        errors['error'].update({ 0 : 'Esse pet nao te pertence... Ainda.'})

    print("------------------")
    print(pet.user_id)
    print(request.user.id)
    print("------------------")
    
    if request.method == 'POST':
        form = PetForm(request.POST,request.FILES, instance=pet)
        form.save()
        return redirect('/system/pets/my' , flag='success')

    return render(request, 'system/editPet.html', {'pet':pet, 'errors':errors , 'form':form})

def petDelete(request, id):
    Pet.objects.filter(id=id).delete()
    return redirect('/system/pets/my')

def adopted(request,id):
    pet = Pet.objects.get(id=id)
    pet.save()
    if(request.user.id == pet.user_id):
        pet.isAdopted = True
        pet.save()
        HttpResponse('success')
    else:
        HttpResponse('Este pet nao te pertence... ainda!')

    return redirect('/system/pets/my')

def success(request): 
    return HttpResponse('successfully uploaded') 