from django.shortcuts import render
from pets.models import Pet

def aboutUs(request):
    return render(request, 'pages/about_us.html' )

def infos(request):
    return render(request, 'pages/informations.html')

def makeafriend(request):
    pets = Pet.objects.all()
    return render(request, 'pages/makeafriend.html', {'pets' : pets})

def HomeView(TemplateView):
    pets = Pet.objects.all()
    return render(TemplateView, "pages/index.html",  {'pets' : pets})

def petDetails(request,id):
    pet = Pet.objects.get(pk=id)
    pet.save()
    return render(request, 'pages/petDetails.html', {'pet':pet})

