from django.urls import path
from .views import SobreNosotros, Contacto, EnviarMensajeView

app_name = 'home_app'

urlpatterns = [
    path(
        "sobre_nosotros/",
        SobreNosotros.as_view(),
        name="sobre_nosotros"
    ),
    path(
        "contacto/",
        Contacto.as_view(),
        name="contacto"
    ),
    path(
        "enviar_mensaje/",
        EnviarMensajeView.as_view(),
        name="enviar_mensaje"
    )
    
]
