from django.shortcuts import render
from .models import Categoria
from django.views.generic import CreateView, DeleteView

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "crear_categoria.html"


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "eliminar_categoria.html"


