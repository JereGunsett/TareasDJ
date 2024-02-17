from django.urls import path
from .views import ComentarioCreateView

app_name = 'comentario_app'

urlpatterns = [
    path(
        "crear/<pk>",
        ComentarioCreateView.as_view(),
        name="crear_comentario"
    ),    
]
