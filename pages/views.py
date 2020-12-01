from django.shortcuts import render
from pets.models import Pet
from users.models import User


def aboutUs(request):
    return render(request, 'pages/about_us.html' )

def infos(request):
    return render(request, 'pages/informations.html')

def makeafriend(request):
    pets = Pet.objects.all()
    return render(request, 'pages/makeafriend.html', {'pets' : pets})

def HomeView(TemplateView):
    pets = Pet.objects.all()
    pets = pets.filter(isAdopted = False)[:6]

    return render(TemplateView, "pages/index.html",  {'pets' : pets})

def petDetails(request,id):
    logged = True
    if not request.user.is_authenticated:
        logged = False
    pet = Pet.objects.get(pk=id)
    pet.save()

    user = User.objects.get(id=pet.user_id)
    user.save()
    try:
        user.mobile_phone = user.mobile_phone.replace('-','').replace('+','') 
    except:
        pass
    
    return render(request, 'pages/petDetails.html', {'pet':pet, 'user':user, 'logged':logged})

