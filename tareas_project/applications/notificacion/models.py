from django.db import models
from django.conf import settings

class Notificacion(models.Model):

    # TODO: Parametros de Notificacion
    usuario_destino = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notificaciones_recibidas')
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Notificacion")
        verbose_name_plural = ("Notificaciones")
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Notificacion para {self.usuario_destino.username}"


