from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Usuario, Video
from .forms import UsuarioForm, VideoForm

class UsuariosView(TemplateView):
    template_name = "usuarios.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['form'] = UsuarioForm()
        return context

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
        else:
            messages.error(request, 'Error al crear el usuario. Verifique los datos.')
    return redirect('Principal:usuariosapp')

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('Principal:usuariosapp')
    else:
        form = UsuarioForm(instance=usuario)
    
    context = {
        'form': form,
        'usuario': usuario,
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios.html', context)

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
    return redirect('Principal:usuariosapp')

class VideosView(TemplateView):
    template_name = "videos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        context['form'] = VideoForm()
        return context

def crear_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video creado exitosamente.')
        else:
            messages.error(request, 'Error al crear el video. Verifique los datos.')
    return redirect('Principal:videosapp')

def editar_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video actualizado exitosamente.')
            return redirect('Principal:videosapp')
    else:
        form = VideoForm(instance=video)
    
    context = {
        'form': form,
        'video': video,
        'videos': Video.objects.all()
    }
    return render(request, 'videos.html', context)

def eliminar_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video eliminado exitosamente.')
    return redirect('Principal:videosapp')