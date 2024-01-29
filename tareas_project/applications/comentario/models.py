from django.db import models
from django.conf import settings
from applications.tarea.models import Tarea

class Comentario(models.Model):

    # TODO: Parametros de Comentario
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.tarea.titulo}"

