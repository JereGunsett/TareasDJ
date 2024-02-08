from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import MensajeContactoForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail



class SobreNosotros(TemplateView):
    template_name = "sobre_nosotros.html"


class Contacto(TemplateView):
    template_name = "contacto.html"

class EnviarMensajeView(FormView):
    template_name = 'contacto.html'
    form_class = MensajeContactoForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        # Obtener datos del formulario
        nombre = form.cleaned_data['nombre']
        correo_electronico = form.cleaned_data['correo_electronico']
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']

        # Construir el cuerpo del correo
        mensaje_correo = f"Nuevo mensaje de contacto:\n\nNombre: {nombre}\nCorreo electrónico: {correo_electronico}\nAsunto: {asunto}\n\nMensaje:\n{mensaje}"

        # Enviar el correo electrónico
        send_mail(
            'Nuevo mensaje de contacto',
            mensaje_correo,
            'tu@email.com',  # Email emisor del mensaje
            ['destinatario@email.com'],  # Email receptor del mensaje
            fail_silently=False,
        )


        print("Correo enviado exitosamente.")
        
        # Redirigir a la página de éxito
        return HttpResponseRedirect(self.get_success_url())

