from functools import partial
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from .models import Proyecto
from .forms import ProyectoForm
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

# def usuario_puede_ver_proyecto(usuario, id_proyecto):
#     # Lógica para determinar si el usuario puede ver el proyecto
#     return usuario.is_superuser or usuario.proyectos_con_permisos.filter(id=id_proyecto).exists()

# usuario_puede_ver_proyecto_requerido = partial(user_passes_test, usuario_puede_ver_proyecto)

class Inicio(TemplateView):
    template_name = 'inicio.html'


class ProyectoListView(ListView):
    model = Proyecto
    template_name = "proyecto/lista.html"
    ordering = 'nombre'
    context_object_name = 'proyectos'

class BuscarProyectoListView(ListView):
    model = Proyecto
    template_name = "proyecto/buscar.html"
    ordering = 'nombre'
    context_object_name = 'proyectos'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Proyecto.objects.filter(
            nombre__icontains = palabra_clave
        )
        return lista
    
# @usuario_puede_ver_proyecto_requerido
class DetalleProyectoListView(DetailView):
    model = Proyecto
    template_name = "proyecto/detalle.html"
    context_object_name = 'detalle'


class ProyectoCreateView(CreateView):
    model = Proyecto
    template_name = "proyecto/crear.html"
    form_class = ProyectoForm
    success_url = reverse_lazy('proyecto_app:Lista de Proyecto')

    def form_valid(self, form):
        body_proyecto = form.save(commit=False)
        body_proyecto.save()
        return super(ProyectoCreateView, self).form_valid(form)
    

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name = "proyecto/modificar.html"
    form_class = ProyectoForm
    success_url = reverse_lazy('proyecto_app:Lista de Proyecto')

    def form_valid(self, form):
        body_proyecto = form.save(commit=False)
        body_proyecto.save()
        return super(ProyectoUpdateView, self).form_valid(form)


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = "proyecto/eliminar.html"
    success_url = reverse_lazy('proyecto_app:Lista de Proyecto')
