from django import forms

class MensajeContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo_electronico = forms.EmailField()
    asunto = forms.CharField(max_length=200)
    mensaje = forms.CharField(widget=forms.Textarea)
