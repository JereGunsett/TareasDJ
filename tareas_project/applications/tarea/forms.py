from django import forms
from django.utils import timezone
from applications.usuario.models import Usuario
from .models import Tarea
from applications.proyecto.models import Proyecto
from django.contrib.auth import get_user_model
from django_select2.forms import ModelSelect2Widget

class UsuarioSelect2Widget(ModelSelect2Widget):
    model = get_user_model()
    search_fields = ['username__icontains', 'first_name__icontains', 'last_name__icontains']
    queryset = Usuario.objects.filter(is_active=True)

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'proyecto', 'categoria', 'usuario_asignado']

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)

        # Establecer la fecha de vencimiento predeterminada a 7 días desde hoy
        self.fields['fecha_vencimiento'].initial = timezone.now() + timezone.timedelta(days=7)

        # Filtrar los proyectos disponibles para la tarea
        self.fields['proyecto'].queryset = Proyecto.objects.all()

        self.fields['usuario_asignado'].queryset = Usuario.objects.filter(is_active=True)
        self.fields['usuario_asignado'].empty_label = '(Seleccionar Usuario)'

        # Utilizar el widget de calendario para el campo fecha_vencimiento
        self.fields['fecha_vencimiento'].widget = forms.TextInput(
            attrs={'type': 'date'}
        )
