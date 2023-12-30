from django.urls import path
from .views import EncuestaCreateView, EncuestaConfirmacion, EncuestaConfirmacionAlumno

app_name = "encuesta"  

urlpatterns = [
    path('encuestas/', EncuestaCreateView.as_view(), name='encuesta_alumno'),
    path('confirmacion/', EncuestaConfirmacion.as_view(), name='encuesta_confirmacion'),
    path('confirm/', EncuestaConfirmacionAlumno.as_view(), name='alumno_confirmacion'),
]
