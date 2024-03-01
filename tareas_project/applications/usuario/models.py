from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    #TODO: Parametros de Usuario 
    #Campos username, password, nombre, apellido y email se encuentran en el modelo AbstractUser
    avatar = models.ImageField('Avatar', upload_to='Usuario', height_field=None, width_field=None, max_length=None, blank=True)
    fecha_registro = models.DateTimeField('Fecha de Registro', auto_now_add=True)
    ultima_conexion = models.DateTimeField('Última Conexión', auto_now=True)

    DEFAULT_AVATAR_PATH = 'Usuario/default_avatar.png'

    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    def save(self, *args, **kwargs):
        # Si el campo avatar está vacío, asigna la imagen por defecto
        if not self.avatar:
            self.avatar = self.DEFAULT_AVATAR_PATH
        super().save(*args, **kwargs)

    def get_proyectos(self):
        return self.proyectos_con_permisos.all()

    def get_tareas_pendientes(self):
        return self.tarea_set.filter(estado='pendiente')
