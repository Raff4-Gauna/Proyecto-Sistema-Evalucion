from django.db import models
from apps.materias.models import Materia
from apps.usuarios.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    docente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
