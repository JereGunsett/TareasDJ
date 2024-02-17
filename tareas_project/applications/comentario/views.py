from django.apps import apps
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Comentario
from .forms import ComentarioForm
from ..usuario.models import Usuario

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/comentario_form.html'
    
    def get_success_url(self):
        return reverse_lazy('comentario_app:crear_comentario', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.autor = Usuario.objects.get(username=self.request.user.username)
        tarea_model = apps.get_model('tarea', 'Tarea')
        tarea_pk = self.kwargs['pk']
        form.instance.tarea = tarea_model.objects.get(pk=tarea_pk)
        return super().form_valid(form)