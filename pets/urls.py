from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.All, name="userInfo"),
    path('/insert', views.insertPets, name="insertPet"),
    path('/my', views.userPets, name="mypets"),
    path('/delete/<int:id>>', views.petDelete, name="deletePet"),
    path('/update/<int:id>', views.editPet, name="EditPet"),

]