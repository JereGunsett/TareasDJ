from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .views import inicio_usuario, inicio



app_name = 'usuario_app'

urlpatterns = [
    path(
        "registro/",
        views.RegistroView.as_view(),
        name="Alta de usuario"
    ),
    path(
        "login/",
        views.UsuarioLoginView.as_view(),
        name="Login de usuario"
    ),
    path(
        "logout/",
        views.UsuarioLogout,
        name="Logout de usuario"
    ),
    path(
        'lista/',
        views.UsuarioListView.as_view(),
        name='Lista de usuario'
    ),
    path(
        'detalle/<pk>',
        views.UsuarioDetailView.as_view(),
        name='Detalle de usuario'
    ),
    path(
        'eliminar/<pk>',
        views.UsuarioDeleteView.as_view(),
        name='Eliminar usuario'
    ),
    path(
        'modificar/<pk>',
        views.UsuarioUpdateView.as_view(),
        name='Modificar usuario'
    ),
    path(
        'inicio/',
        inicio_usuario,
        name='Inicio de usuario'
    ),
    path(
        '',
        inicio,
        name='Inicio'
    ),
    path(
        "password_reset/",
        views.UsuarioPasswordResetView.as_view(),
        name="Reinicio de Contraseña"
    ),
    path(
        "password_reset/done/",
        views.UsuarioPasswordResetDoneView.as_view(),
        name="Reinicio de Contraseña echo"
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.UsuarioPasswordResetConfirmView.as_view(),
        name="Confirmacion de reinicio de contraseña"
    ),
    path(
        "reset/done/",
        views.UsuarioPasswordResetCompleteView.as_view(),
        name="Reinicio Completo"
    )
    
    
    
    
]
