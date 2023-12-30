from django.db import models
from apps.usuarios.models import User
from apps.carrera.models import Carrera
from apps.materias.models import Materia

VERIFICATION_OPTIONS = (
    ('unverified', 'Unverified'),
    ('verified', 'Verified'),
)
VERIFICATION_ROLES = (
    ('standard', 'Standard'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
)

class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carreras = models.ManyToManyField(Carrera, related_name='docentes')
    materias = models.ManyToManyField(Materia, related_name='docentes')
    role = models.CharField(max_length=15, choices=VERIFICATION_ROLES, default='Standard')
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='Unverified')

    def __str__(self):
        return self.user.username
