from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    """Form definition for Comentario."""

    class Meta:
        """Meta definition for Comentarioform."""

        model = Comentario
        fields = ('contenido',)
        widgets ={
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        }
