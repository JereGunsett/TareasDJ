from django import forms
from .models import Proyecto


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
            'usuarios_con_permisos': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }