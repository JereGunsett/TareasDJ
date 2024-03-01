from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioRegistroForm(UserCreationForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')  # Remove the password confirmation field
        self.fields['password1'].required = False  # Password is not required for update

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user