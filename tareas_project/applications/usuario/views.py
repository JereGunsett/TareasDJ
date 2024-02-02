from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from applications.proyecto.models import Proyecto
from applications.tarea.models import Tarea
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .forms import UsuarioRegistroForm
from .models import Usuario

class UsuarioListView(ListView):
    model = Usuario
    template_name = "usuario/lista.html"
    context_object_name = "usuarios"

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "usuario/detalle.html"
    context_object_name = "usuario"


class RegistroView(CreateView):
    form_class = UsuarioRegistroForm  # formulario de registro
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('usuario_app:Lista de usuario')  # ruta a la plantilla de registro

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
    
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = "usuario/modificar.html"
    form_class = UsuarioRegistroForm
    success_url = reverse_lazy('usuario_app:Lista de usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupos'] = self.object.groups.all()
        context['permisos'] = self.object.user_permissions.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            avatar = request.FILES.get('avatar')
            if avatar:
                form.instance.avatar = avatar
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        
        # Obtener grupos y permisos desde el formulario
        grupos = self.request.POST.getlist('groups')
        permisos = self.request.POST.getlist('user_permissions')

        # Asignar grupos y permisos al usuario
        user.groups.set(grupos)
        user.user_permissions.set(permisos)
        user.save()

        login(self.request, user)
        return response
    
    
class UsuarioLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'usuario/login.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

def UsuarioLogout(request):
    logout(request)
    return redirect('inicio')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "usuario/eliminar.html"
    success_url = reverse_lazy('usuario_app:Lista de usuario')

@login_required
def inicio_usuario(request):
    # Obtener las tareas pendientes y proyectos del usuario
    tareas_pendientes = Tarea.objects.filter(usuario_asignado=request.user, estado='pendiente')
    proyectos = request.user.get_proyectos()


    print(f"Tareas Pendientes: {tareas_pendientes}")
    print(f"Proyectos: {proyectos}")

    return render(request, 'inicio.html', {'tareas_pendientes': tareas_pendientes, 'proyectos': proyectos})

def inicio(request):
    if request.user.is_authenticated:
        usuario = request.user
        proyectos = usuario.proyectos_con_permisos.all()
        tareas_pendientes = Tarea.objects.filter(usuario_asignado=usuario, estado='pendiente')
        return render(request, 'inicio.html', {'proyectos': proyectos, 'tareas_pendientes': tareas_pendientes})
    else:
        return render(request, 'inicio.html')

class UsuarioPasswordResetView(PasswordResetView):
    template_name = 'usuario/password_reset.html'
    email_template_name = 'usuario/password_reset_email.html'
    subject_template_name = 'usuario/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class UsuarioPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'usuario/password_reset_done.html'

class UsuarioPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'usuario/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class UsuarioPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'usuario/password_reset_complete.html'