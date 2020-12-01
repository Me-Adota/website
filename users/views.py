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


    # if(user.cpf == '' or user.full_name == '' or user.mobile_phone == '' or user.zip_code == ''):
    #     errors = { 'has_errors' : 1 } 
    #     errors['error'].update({ 0 : 'Antes de adicionar um pet para adoção é necessário que você complete o seu cadastro!'})

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
            print("-----------------------")
            # errors['has_errors'] = 0 

            print(errors)
            print("-----------------------")
            if(errors['has_errors'] == 0):
                user.full_name = str(data['full_name'])
                user.cpf = str(data['cpf'])
                user.address1 = str(data['address1'])
                user.address2 = str(data['address2'])
                if(str(data['date_of_birth']) != ''):
                    
                    user.date_of_birth = str(data['date_of_birth'])
                user.zip_code = str(data['zip_code'])
                user.city = str(data['city'])
                user.country = str(data['country'])
                user.mobile_phone = str(data['mobile_phone'])
                user.additional_information = str(data['additional_information'])
                user.save()

                redirect('system/personal.html')
        except:
            print("----------ERRROR-------------")
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

    if('zip_code' in data and data['zip_code'] != ''):
        if(len(data['zip_code']) < 9):
            errors['has_errors'] = 1
            errors['error'].update({ index : 'Cep não válido por favor verifique novamente, ou deixe o campo em branco'})
            index+=1

    if('date_of_birth' in data and data['date_of_birth'] != ''):
        if(len(data['date_of_birth']) < 10):
            errors['has_errors'] = 1
            errors['error'].update({ index : 'Data de nascimento não válido por favor verifique novamente, ou deixe o campo em branco'})
            index+=1
        try:
            verify_date = data['date_of_birth'].split('-')
            if(int(verify_date[0]) < 1800 or int(verify_date[1]) > 12 or int (verify_date[2]) > 31 ):
                errors['has_errors'] = 1
                errors['error'].update({ index : 'Por favor verifique novamente se a data está no formato YYYY-MM-DD Ex: 2004-12-31'})
                index+=1
        except:
            pass

    if('mobile_phone' in data and data['mobile_phone'] != ''):
        if(len(data['mobile_phone']) < 15):
            errors['has_errors'] = 1
            errors['error'].update({ index : 'Numero de telefone não válido por favor verifique novamente, ou deixe o campo em branco'})
            index+=1
    return errors

def logout_view(request):
    logout(request)
    return redirect('/')

