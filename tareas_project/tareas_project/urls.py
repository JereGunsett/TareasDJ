"""tareas_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from applications.proyecto.views import Inicio
from django.contrib.auth.views import LoginView, LogoutView
from applications.usuario.views import RegistroView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',Inicio.as_view(), name='inicio'),
    path('admin/', admin.site.urls),
    re_path('proyecto/', include('applications.proyecto.urls')),
    re_path('usuario/', include('applications.usuario.urls')),
    re_path('tarea/', include('applications.tarea.urls')),
    re_path('home/', include('applications.home.urls')),
    re_path('comentario/', include('applications.comentario.urls')),
    path('select2/', include('django_select2.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + staticfiles_urlpatterns()


# urlpatterns += staticfiles_urlpatterns()