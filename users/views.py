from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import User
from .forms import UserEditForms
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from validate_docbr import CPF



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

    form = UserEditForms(instance=user)
    errors = {}
    errors = { 'has_errors' : 0 } 

    if(user.cpf == '' or user.full_name == '' or user.mobile_phone == '' ):
        errors = { 'has_errors' : 1 } 
        errors['error'] = {}
        if(user.cpf == ''):
            errors['error'].update({ 0 : 'Antes de cadastrar um pet para adoção é necessário que você insira seu CPF'})
        if(user.full_name == ''):
            errors['error'].update({ 1 : 'Antes de cadastrar um pet para adoção é necessário que você insira seu nome!'})
        if(user.mobile_phone == ''):
            errors['error'].update({ 2 : 'Antes de cadastrar um pet para adoção é necessário que insira seu telefone!'})

    if request.method == 'POST':
        print(request.POST)
        try:
            if 'photo' in request.FILES :
                myfile = request.FILES['photo']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                user.photo = uploaded_file_url
            data = request.POST

            errors = validate_fields(data, errors)    
            if(errors['has_errors'] == 0):
                user.full_name = str(data['full_name'])
                user.cpf = str(data['cpf'])
                user.mobile_phone = str(data['mobile_phone'])
                user.save()
                # return HttpResponseRedirect('%s?%s' % ('system/pets/my', "?update=success"))

                response = redirect('/system/pets/my')
                response['Location'] += '?update=success'
                return response

        except:
            print(traceback.format_exc())
            return redirect('system/personal')

    return render(request, 'system/personal.html', {'user':user , 'form':form, 'errors' : errors})

def validate_fields(data, errors):
    errors['has_errors'] = 0
    errors['error'] = {}
    index = 0 


    if('cpf' in data and data['cpf'] != ''):
        cpf = CPF()
        cpf_valid = cpf.validate(data['cpf'])
        if(cpf_valid == False):
            errors['has_errors'] = 1
            errors['error'].update({ index : 'CPF não válido por favor verifique novamente, ou deixe o campo em branco'})
            index+=1

    if('mobile_phone' in data and data['mobile_phone'] != ''):
        if(len(data['mobile_phone']) < 15):
            errors['has_errors'] = 1
            errors['error'].update({ index : 'Numero de telefone não válido por favor verifique novamente, ou deixe o campo em branco'})
            index+=1
    return errors

def logout_view(request):
    logout(request)
    return redirect('/')