from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import User
import traceback

# Create your views here.
def PersonalProfile(request):
    if not request.user.is_authenticated:
        print("Thiis is a not logged user bro:")
        return redirect('/accounts/login/')
    else:
        print("successfully logged")
    user = User.objects.get(pk=request.user.id)
    user.save()

    if not request.user.is_authenticated:
        return render(request, '')
    if request.method == 'POST':
        try:
            data = request.POST
            
            user.email = str(data['email'])
            user.full_name = str(data['full_name'])
            if(data['password']  != ""):
                user.password = str(data['password'])
            user.address1 = str(data['address1'])
            user.address2 = str(data['address2'])
            user.zip_code = str(data['zip_code'])
            user.city = str(data['city'])
            user.country = str(data['country'])
            user.phone_regex = str(data['phone_regex'])
            user.mobile_phone = str(data['mobile_phone'])
            user.additional_information = str(data['additional_information'])
            user.save()
        except:
            print(traceback.format_exc())
            return render(request, 'redirect_404.html', {})

    return render(request, 'system/personal.html', {"user" : user})


def logout_view(request):
    logout(request)
    return redirect('/')

