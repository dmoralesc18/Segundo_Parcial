from django.contrib import admin
from django.urls import path , include
from Apps.Home import views
from .views import HomeView , CreditosView

urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('creditos/', CreditosView.as_view(), name='creditosapp'),
]
