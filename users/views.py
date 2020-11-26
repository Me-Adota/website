from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import User,UserManager
# Create your views here.
# Create your views here.
def PersonalProfile(request):
    if not request.user.is_authenticated:
        print("Thiis is a not logged user bro:")
        return redirect('/accounts/login/')
    else:
        print("successfully logged")
    user = User.objects.get(pk=request.user.id)

    return render(request, 'system/personal.html', {"user" : user})

        

def addPersonalInfo(request):
    if not request.user.is_authenticated:
        return render(request, '')
    try:
        data = request.POST
        user = User.objects.create(email = data['email'], full_name = data['full_name'], password = data['password'])
        user.save()
    except:
        return render(request, 'redirect_404.html', {})
        raise ValueError("Inserction failed")
        ''
    else:
       ''
    return HttpResponse(user)


def updatePersonalInfo(request):
    if not request.user.is_authenticated:
        return render(request, '')
    u = User.objects.get(id=request.user.id)
    data = request.POST
    u.set_password(data['password'])
    user = User.objects.create(email = data['email'], full_name = data['full_name'], password = data['password'])
    user.save()


def logout_view(request):
    logout(request)
    return redirect('/')