from django import forms
from django_select2.forms import ModelSelect2Widget
from .models import Proyecto
from django.contrib.auth import get_user_model

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = (
            "nombre",
            "descripcion",
            "fecha_inicio",
            "fecha_fin",
            "estado",
            "usuarios_con_permisos"
        )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'usuarios_con_permisos': ModelSelect2Widget(
                model=get_user_model(),
                search_fields=['username__icontains', 'first_name__icontains', 'last_name__icontains'],
                attrs={'style': 'width: 100%;'}
            )
        }