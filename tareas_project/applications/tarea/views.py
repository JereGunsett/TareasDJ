from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea
from .forms import TareaForm


class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea/tarea_list.html'
    context_object_name = 'tareas'
    ordering = ['-fecha_creacion']

class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'tarea/tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/tarea_form.html'
    success_url = reverse_lazy('tarea_app:Lista de Tarea')

    def form_valid(self, form):
        body_tarea = form.save(commit=False)
        body_tarea.save()
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
