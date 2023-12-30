# Generated by Django 3.2.6 on 2023-11-21 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materias', '0001_initial'),
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.materia'),
        ),
    ]