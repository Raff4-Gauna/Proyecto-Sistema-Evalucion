from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.usuarios.models import User
from apps.materias.models import Materia
from django.core.exceptions import ValidationError
from django.utils import timezone
# Definición de respuestas 
TIPO_RESPUESTAS_CHOICES = (
    ('si', 'Sí'),
    ('no', 'No'),
    ('tal vez', 'Tal Vez'),
    ('prefiero no responder', 'Prefiero no responder'),
)

def validate_respuesta(value):
    if value not in dict(TIPO_RESPUESTAS_CHOICES).keys():
        raise ValidationError('Respuesta no válida')

# Genero las preguntas
class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.texto_pregunta
    
class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=50, choices=TIPO_RESPUESTAS_CHOICES, validators=[validate_respuesta])
    contador = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pregunta}: {self.respuesta}"

class Encuesta(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    respuestas = models.ManyToManyField(Respuesta, related_name='encuestas_respuestas')

    def __str__(self):
        return f"Encuesta de {self.usuario} en {self.materia}"
    

class RespuestaEncuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='respuestas_encuesta')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=50)  # Puedes cambiar este campo según tu nueva lógica

    def __str__(self):
        return f"Respuesta '{self.respuesta}' en {self.encuesta} para {self.pregunta}"

