from django.db import models

class Categoria(models.Model):

    # TODO: Parametros de Categoria 
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.nombre

