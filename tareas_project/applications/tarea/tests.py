from django.utils import timezone
from django.test import TestCase
from applications.categoria.models import Categoria
from applications.proyecto.models import Proyecto
from applications.tarea.models import Tarea
from applications.usuario.models import Usuario

class TareaModelTestCase(TestCase):
    def setUp(self):
        #Se crea objeto de prueba:
        proyecto = Proyecto.objects.create(nombre="Proyecto de Prueba")
        categoria = Categoria.objects.create(nombre="Categoria de Prueba")
        usuario = Usuario.objects.create(username="Usuario_prueba")

        Tarea.objects.create(
            titulo = "Tarea de Prueba",
            descripcion = "Descripcion de la tarea de prueba",
            fecha_creacion = timezone.now(),
            fecha_vencimiento = timezone.now() + timezone.timedelta(days=7),
            estado = 'pendiente',
            proyecto = proyecto,
            usuario_asignado = usuario,
            categoria = categoria
        )

        def test_tarea_str(self):
            tarea = Tarea.objects.get(titulo="Tarea de prueba")
            self.assertEqual(str(tarea), tarea.titulo)

        def test_tarea_estado_default(self):
            tarea = Tarea.objects.get(titulo="Tarea de prueba")
            self.assertEqual(tarea.estado, 'pendiente')