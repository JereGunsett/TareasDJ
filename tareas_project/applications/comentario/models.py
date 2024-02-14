from django.db import models
from django.conf import settings

class Comentario(models.Model):

    # TODO: Parametros de Comentario
    tarea = models.ForeignKey('tarea.Tarea', on_delete=models.CASCADE, related_name='tarea_comentarios')
    autor = models.ForeignKey('usuario.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.tarea.titulo}"

