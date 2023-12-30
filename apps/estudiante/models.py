from django.db import models
from apps.carrera.models import Carrera
from apps.usuarios.models import User


VERIFICATION_ROLES = (
    ('standard', 'Standard'),
    ('student', 'Student'),
)

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=VERIFICATION_ROLES, default='Standard')

    def __str__(self):
        return self.user.username
