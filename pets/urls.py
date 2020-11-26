from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.All, name="userInfo"),
    path('insert', views.insertPets, name="insertPet"),
    path('mypets', views.userPets, name="mypets"),
]