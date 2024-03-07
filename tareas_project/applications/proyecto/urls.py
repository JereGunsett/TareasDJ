from django.contrib import admin
from django.urls import path, re_path, include
from . import views


app_name = 'proyecto_app'

urlpatterns = [
    path(
        "lista/",
        views.ProyectoListView.as_view(),
        name="Lista de Proyecto"
    ),
    path(
        "buscar/",
        views.BuscarProyectoListView.as_view(),
        name="Buscar Proyecto"
    ),
    path(
        "detalle/<pk>",
        views.DetalleProyectoListView.as_view(),
        name="Detalle del Proyecto"
    ),
    path(
        "crear/",
        views.ProyectoCreateView.as_view(),
        name="Alta de Proyecto"
    ),
    path(
        "modificar/<pk>",
        views.ProyectoUpdateView.as_view(),
        name="Modificar Proyecto"
    ),
    path(
        "eliminar/<pk>",
        views.ProyectoDeleteView.as_view(),
        name="Eliminar Proyecto"
    ),
    path(
        "lista/api",
        views.ProyectoListApiView.as_view(),
        name="Lista API"
    )
    
]
