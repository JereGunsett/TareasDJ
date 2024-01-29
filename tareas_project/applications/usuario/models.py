from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.admin.models import LogEntry

# Create your models here.
class Usuario(AbstractUser):

    #Campos username, password, nombre, apellido y email se encuentran en el modelo AbstractUser
    
    avatar = models.ImageField('Avatar', upload_to='Usuario', height_field=None, width_field=None, max_length=None, blank=True)
    fecha_registro = models.DateTimeField('Fecha de Registro', auto_now_add=True)
    ultima_conexion = models.DateTimeField('Última Conexión', auto_now=True)

    DEFAULT_AVATAR_PATH = 'Usuario/default_avatar.png'

    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username}"
    

    def save(self, *args, **kwargs):
        # Si el campo avatar está vacío, asigna la imagen por defecto
        if not self.avatar:
            self.avatar = self.DEFAULT_AVATAR_PATH
        super().save(*args, **kwargs)
