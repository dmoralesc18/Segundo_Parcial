from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Email")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return self.nombre

class Video(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    url = models.URLField(verbose_name="URL del Video")
    descripcion_contenido = models.TextField(verbose_name="Descripción de que trata", help_text="Describe brevemente de qué trata el video")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Subida")
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-fecha_subida']
    
    def __str__(self):
        return self.titulo