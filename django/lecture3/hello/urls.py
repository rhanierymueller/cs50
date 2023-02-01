#Quer sera uma lista de todas as URLS permitidas que podem ser acessadas para este 
#aplicativo especifico 

#from django import views
from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("rhaniery", views.rhaniery, name="rhaniery"),
    path("david", views.david, name="david")
]