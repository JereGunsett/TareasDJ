from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario

class UsuarioRegistroForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'is_active', 
            'is_staff',   
            'is_superuser',
            'groups',
            'user_permissions',
        )
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user