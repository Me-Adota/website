from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.PersonalProfile, name="userInfo"),
    path('insert', views.addPersonalInfo, name='addInfo'),
    path('update', views.addPersonalInfo, name='updateInfo'),
    path('logout', views.logout_view, name='logout')
]