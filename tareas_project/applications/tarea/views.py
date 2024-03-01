from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea
from .forms import TareaForm
from applications.comentario.forms import ComentarioForm


class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea/tarea_list.html'
    context_object_name = 'tareas'
    ordering = ['-fecha_creacion']

    def get_queryset(self):
            palabra_clave = self.request.GET.get('kword','')
            lista = Tarea.objects.filter(
                titulo__icontains = palabra_clave
            )
            return lista

class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'tarea/tarea_detail.html'
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object is not None:
            context['comentarios'] = self.object.tarea_comentarios.all().order_by('-fecha_creacion')
        else:
            context['mensaje_no_comentarios'] = "Esta tarea no tiene comentarios."
        context['form_comentario'] = ComentarioForm()

        # Mensaje informativo si no hay comentarios
        if not context['comentarios']:
            context['mensaje_no_comentarios'] = "Esta tarea no tiene comentarios."

        return context

class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/tarea_form.html'
    success_url = reverse_lazy('tarea_app:Lista de Tarea')

    def form_valid(self, form):
        print("Formulario válido")
        if form.is_valid():
            print("El formulario es válido")
        else:
            print("Errores en el formulario:", form.errors)
        body_tarea = form.save(commit=False)
        body_tarea.save()
        print("Tarea guardada:", body_tarea)
        return super(TareaCreateView, self).form_valid(form)

class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/tarea_form.html'
    success_url = reverse_lazy('tarea_app:Lista de Tarea')

class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tarea/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea_app:Lista de Tarea')
