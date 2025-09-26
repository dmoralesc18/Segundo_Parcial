from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class UsuariosView(TemplateView):
    template_name = "usuarios.html"

class VideosView(TemplateView):
    template_name = "videos.html"