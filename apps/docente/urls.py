from django.urls import path
from .views import DocenteEncuestasView

app_name = "docente"  

urlpatterns = [
    path('consultar/', DocenteEncuestasView.as_view(), name='consulta_encuesta'),
]