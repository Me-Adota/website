from django.shortcuts import render
from pets.models import Pet
from users.models import User
from pets.filters import *
from django.core.paginator import Paginator



def aboutUs(request):
    return render(request, 'pages/about_us.html' )

def infos(request):
    qtd_pets = Pet.objects.filter(isAdopted=False).count()
    qtd_adopted = Pet.objects.filter(isAdopted=True).count()
    qtd_vulnerable = Pet.objects.filter(vulnerable=True, isAdopted=False).count()
    qtd_users = User.objects.all().count()

    return render(request, 'pages/informations.html', {'qtd_vulnerable':qtd_vulnerable, 'qtd_pets':qtd_pets, 'qtd_adopted':qtd_adopted, 'qtd_users':qtd_users})

def makeafriend(request):
    pets = Pet.objects.all().filter(isAdopted = False)

    myFilter = PetFilter(request.GET, queryset = pets)
    pets = myFilter.qs.order_by('vulnerable').reverse()
    paginator = Paginator(pets, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    pets = paginator.get_page(page_number)
    # context{'pet':pet,'myFilter':myFilter}
    return render(request, 'pages/makeafriend.html', {'pets' : pets, 'myFilter':myFilter})

def HomeView(TemplateView):
    pets = Pet.objects.all()
    pets = pets.filter(isAdopted = False).order_by('vulnerable').reverse()[:6]

    qtd_pets = Pet.objects.filter(isAdopted=False).count()
    qtd_adopted = Pet.objects.filter(isAdopted=True).count()
    qtd_vulnerable = Pet.objects.filter(vulnerable=True, isAdopted=False).count()
    qtd_users = User.objects.all().count()

    return render(TemplateView, "pages/index.html",  {'pets' : pets, 'qtd_vulnerable':qtd_vulnerable, 'qtd_pets':qtd_pets, 'qtd_adopted':qtd_adopted, 'qtd_users':qtd_users})

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