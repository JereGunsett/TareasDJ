from django.apps import apps
from django.db import models
from applications.categoria.models import Categoria
from applications.proyecto.models import Proyecto
from applications.usuario.models import Usuario

class Tarea(models.Model):

    # TODO: Opciones de Estados
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
    ]

    # TODO: Parametros de Tarea
    titulo = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)
    usuario_asignado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    comentarios = models.ManyToManyField('comentario.Comentario', related_name='comentarios', blank=True)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.titulo

