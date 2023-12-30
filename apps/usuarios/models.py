# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# VERIFICATION_OPTIONS = (
#     ('unverified', 'Unverified'),
#     ('verified', 'Verified'),
# )
# VERIFICATION_ROLES = (
#     ('standard', 'Standard'),
#     ('student', 'Student'),
#     ('teacher', 'Teacher'),
# )

# class User(AbstractUser):
#     image = models.ImageField(upload_to='users', null=True, blank=True)
#     biography = models.TextField(max_length=500, blank=True)
#     role = models.CharField(max_length=15, choices=VERIFICATION_ROLES, default='Standard')
#     verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='Unverified')

#     def __str__(self):
#         return self.username

# @receiver(post_save, sender=User)
# def assign_default_image(sender, instance, **kwargs):
#     if not instance.image:
#         instance.image = 'perfil-default.png'
#         instance.save()

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save



class User(AbstractUser):
    image = models.ImageField(upload_to='users', null=True, blank=True)
    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def assign_default_image(sender, instance, **kwargs):
    if not instance.image:
        instance.image = 'perfil-default.png'
        instance.save()
