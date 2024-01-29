from django.contrib import admin
from django.urls import path, re_path, include
from . import views


app_name = 'tarea_app'

urlpatterns = [
    path(
        "lista/",
        views.TareaListView.as_view(),
        name="Lista de Tarea"
    ),
    path(
        "detalle/<pk>",
        views.TareaDetailView.as_view(),
        name="Detalle de Tarea"
    ),
    path(
        "crear/",
        views.TareaCreateView.as_view(),
        name="Crear Tarea"
    ),
    path(
        "modificar/<pk>",
        views.TareaUpdateView.as_view(),
        name="Modificar Tarea"
    ),
    path(
        "eliminar/<pk>",
        views.TareaDeleteView.as_view(),
        name="Eliminar Tarea"
    )
]
