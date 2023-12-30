# # admin.py
# from django.contrib import admin
# from .models import Pregunta, Respuesta, Encuesta, RespuestaEncuesta

# class RespuestaInline(admin.TabularInline):
#     model = Respuesta
#     extra = 0

# class RespuestaEncuestaInline(admin.TabularInline):
#     model = RespuestaEncuesta
#     extra = 0

# class EncuestaAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'materia', 'fecha', 'preguntas_respuestas')
#     inlines = [RespuestaEncuestaInline]

#     def preguntas_respuestas(self, obj):
#         # Concatenar todas las preguntas y respuestas en una cadena
#         return '\n'.join([f"{respuesta.pregunta.texto_pregunta}: {respuesta.respuesta.respuesta}" for respuesta in obj.respuestas_encuesta.all()])

#     preguntas_respuestas.short_description = 'Preguntas y Respuestas'

# admin.site.register(Pregunta)
# admin.site.register(Respuesta)
# admin.site.register(Encuesta, EncuestaAdmin)


from django.contrib import admin
from .models import Pregunta, Respuesta, Encuesta, RespuestaEncuesta

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]

class RespuestaEncuestaInline(admin.TabularInline):
    model = RespuestaEncuesta
    extra = 1

class EncuestaAdmin(admin.ModelAdmin):
    inlines = [RespuestaEncuestaInline]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
