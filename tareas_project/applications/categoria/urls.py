from django.urls import path
from .views import CategoriaCreateView, CategoriaDeleteView

app_name = 'categoria_app'

urlpatterns = [
    path(
        "crear_categoria/",
        CategoriaCreateView.as_view(),
        name="crear_categoria"
    ),
    path(
        "eliminar_categoria/",
        CategoriaDeleteView.as_view(),
        name="eliminar_categoria"
    )
]
