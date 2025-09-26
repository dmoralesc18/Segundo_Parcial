from django.urls import path
from Apps.Principal import views
from .views import UsuariosView, VideosView

app_name = 'Principal'

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuariosapp'),
    path('usuario/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuario/crear-form/', views.crear_usuario_form, name='crear_usuario_form'),
    path('usuario/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuario/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('videos/', VideosView.as_view(), name='videosapp'),
    path('video/crear/', views.crear_video, name='crear_video'),
    path('video/crear-form/', views.crear_video_form, name='crear_video_form'),
    path('video/editar/<int:pk>/', views.editar_video, name='editar_video'),
    path('video/eliminar/<int:pk>/', views.eliminar_video, name='eliminar_video'),
]