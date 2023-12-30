# from django import forms
# from .models import Encuesta, Pregunta, Respuesta, TIPO_RESPUESTAS_CHOICES

# class EncuestaForm(forms.ModelForm):
#     class Meta:
#         model = Encuesta
#         fields = ['materia']  # Agrega los campos que deseas mostrar en el formulario

#     def __init__(self, *args, **kwargs):
#         super(EncuestaForm, self).__init__(*args, **kwargs)

#         # Añadir campos de pregunta y respuestas al formulario
#         preguntas = Pregunta.objects.all()
#         for pregunta in preguntas:
#             respuestas_field_name = f"respuesta_{pregunta.id}"
#             choices = [(respuesta, respuesta) for respuesta, _ in TIPO_RESPUESTAS_CHOICES]

#             self.fields[respuestas_field_name] = forms.ChoiceField(
#                 label=pregunta.texto_pregunta,
#                 choices=choices,
#                 widget=forms.RadioSelect,
#                 required=True
#             )

#     def clean(self):
#         cleaned_data = super(EncuestaForm, self).clean()

#         # Validar lógica de negocio específica si es necesario

#         return cleaned_data


from django import forms
from .models import Encuesta, Pregunta, Respuesta, RespuestaEncuesta, TIPO_RESPUESTAS_CHOICES

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['materia']

    def __init__(self, *args, **kwargs):
        super(EncuestaForm, self).__init__(*args, **kwargs)

        preguntas = Pregunta.objects.all()
        for pregunta in preguntas:
            respuestas_field_name = f"respuesta_{pregunta.id}"
            choices = [(respuesta, respuesta) for respuesta, _ in TIPO_RESPUESTAS_CHOICES]

            self.fields[respuestas_field_name] = forms.ChoiceField(
                label=pregunta.texto_pregunta,
                choices=choices,
                widget=forms.RadioSelect,
                required=True
            )

    def clean(self):
        cleaned_data = super(EncuestaForm, self).clean()

        # Agregar la lógica específica de tu aplicación si es necesario

        return cleaned_data

    def save(self, commit=True):
        # Guardar la encuesta
        encuesta = super().save(commit=False)
        encuesta.usuario = self.instance.usuario  # Obtener el usuario del formulario
        if commit:
            encuesta.save()

        # Guardar las respuestas
        for pregunta in Pregunta.objects.all():
            respuestas_field_name = f"respuesta_{pregunta.id}"
            respuesta = RespuestaEncuesta(
                encuesta=encuesta,
                pregunta=pregunta,
                respuesta=self.cleaned_data[respuestas_field_name]
            )
            respuesta.save()

        return encuesta