from django.db import models
from django.conf import settings

class Proyecto(models.Model):

    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('detenido ', 'Detenido'),
        ('finalizado', 'Finalizado'),
    ]

    # TODO: Parametros de Proyecto
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    usuarios_con_permisos = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='proyectos_con_permisos', blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre

