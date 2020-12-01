from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.HomeView),
    path('aboutus', views.aboutUs, name="aboutUs"),
    path('informations', views.infos, name="infos"),
    path('home', views.HomeView, name = "home"),
    path('makeafriend', views.makeafriend, name = 'makeafriend'),    
    path('details/<int:id>', views.petDetails, name="Details"),
]

