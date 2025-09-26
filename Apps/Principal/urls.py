from django.contrib import admin
from django.urls import path , include
from Apps.Principal import views
from .views import UsuariosView, VideosView

app_name = 'Principal'

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuariosapp'),
    path('videos/', VideosView.as_view(), name='videosapp'),
]
