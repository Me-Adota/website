from django.shortcuts import render
from pets.models import Pet
from pets.filters import *

def aboutUs(request):
    return render(request, 'pages/about_us.html' )

def infos(request):
    return render(request, 'pages/informations.html')

def makeafriend(request):
    pets = Pet.objects.all()

    myFilter = PetFilter(request.GET, queryset = pets)

    pets = myFilter.qs
    # context{'pet':pet,'myFilter':myFilter}
    return render(request, 'pages/makeafriend.html', {'pets' : pets, 'myFilter':myFilter})

def HomeView(TemplateView):
    pets = Pet.objects.all()
    return render(TemplateView, "pages/index.html",  {'pets' : pets})

def petDetails(request,id):
    pet = Pet.objects.get(pk=id)
    pet.save()
    return render(request, 'pages/petDetails.html', {'pet':pet})

