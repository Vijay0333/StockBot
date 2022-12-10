from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path("",views.index, name ="home"),
    path("index2.html",views.index, name ="home"),
    path("About.html",views.about, name ="about"),
    path("Market.html",views.services, name ="service"),
    path("Contect.html",views.Contect, name ="Contect"),
    path("SharePrise.html",views.Sprise, name ="Prise"),
    path("Trade.html",views.Trade, name ="Trade"),
]