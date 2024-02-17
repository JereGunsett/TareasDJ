from django.db import models
from django.utils import timezone
from applications.usuario.models import Usuario

class Proyecto(models.Model):

    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Detenido ', 'Detenido'),
        ('Finalizado', 'Finalizado'),
    ]

    # TODO: Parametros de Proyecto
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField(default=timezone.now().date())
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activo')
    usuarios_con_permisos = models.ManyToManyField(Usuario, related_name='proyectos_con_permisos', blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre

