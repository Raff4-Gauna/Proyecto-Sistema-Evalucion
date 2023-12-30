from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Encuesta
from .forms import EncuestaForm
from apps.carrera.models import Carrera
from apps.materias.models import Materia
from django.urls import reverse_lazy
from django.contrib import messages


# class EncuestaCreateView(View):
#     template_name = 'components/surveys/student_survey.html'
#     survey_not_available_template = 'components/surveys/survey_not_available.html'

#     def _check_survey_existence(self, user):
#         return Encuesta.objects.filter(usuario=user).exists()

#     def _get_user_career_and_subjects(self, user):
#         # Obtener la carrera del alumno
#         carrera_alumno = user.estudiante.carrera

#         # Obtener las materias asociadas a la carrera del alumno
#         materias_carrera = Materia.objects.filter(carrera=carrera_alumno)

#         return carrera_alumno, materias_carrera

#     def get(self, request, *args, **kwargs):
#         # Verificar que el usuario es un alumno
#         if request.user.is_authenticated and request.user.role == 'student':
#             # Verificar si el alumno ya ha respondido la encuesta
#             if self._check_survey_existence(request.user):
#                 return render(request, self.survey_not_available_template)

#             # Obtener la carrera del alumno y las materias asociadas
#             carrera_alumno, materias_carrera = self._get_user_career_and_subjects(request.user)

#             # Crear un formulario de encuesta para el usuario actual
#             form = EncuestaForm()

#             # Pasar el formulario y las materias al contexto
#             context = {'form': form, 'materias': materias_carrera}
#             return render(request, self.template_name, context)
#         else:
#             # Redirigir a la página de inicio de sesión si el usuario no es un alumno
#             return redirect('usuarios:login_user')
        
#     def post(self, request, *args, **kwargs):
#         # Verificar que el usuario es un alumno
#         if request.user.is_authenticated and request.user.role == 'student':
#             # Verificar si el alumno ya ha respondido la encuesta
#             encuesta_existente = Encuesta.objects.filter(usuario=request.user).exists()

#             if encuesta_existente:
#                 return render(request, self.survey_not_available_template)

#             # Obtener la carrera del alumno
#             carrera_alumno = request.user.estudiante.carrera

#             # Obtener las materias asociadas a la carrera del alumno
#             materias_carrera = Materia.objects.filter(carrera=carrera_alumno)

#             # Crear un formulario de encuesta con los datos enviados en el formulario POST
#             form = EncuestaForm(request.POST)

#             # Validar el formulario
#             if form.is_valid():
#                 # Crear una instancia de la encuesta y asociarla al alumno actual
#                 encuesta = form.save(commit=False)
#                 encuesta.usuario = request.user  # Asignar el usuario actual
#                 encuesta.save()
#                 # Redirigir directamente a la página de confirmación
#                 messages.success(request, '¡Gracias por responder! Tus respuestas han sido registradas. Agradecemos tu participación.')
#                 return redirect('encuesta:encuesta_confirmacion')

#             # Si el formulario no es válido, volver a renderizar la página con el formulario y las materias
#             context = {'form': form, 'materias': materias_carrera}
#             return render(request, self.template_name, context)
#         else:
#             # Redirigir a la página de inicio de sesión si el usuario no es un alumno
#             return redirect('usuarios:login_user')


# 
class EncuestaCreateView(View):
    template_name = 'components/surveys/student_survey.html'
    survey_not_available_template = 'components/surveys/survey_not_available.html'
    success_message = '¡Gracias por responder! Tus respuestas han sido registradas. Agradecemos tu participación.'

    def _check_survey_existence(self, user):
        return Encuesta.objects.filter(usuario=user).exists()

    def _get_user_career_and_subjects(self, user):
        carrera_alumno = user.estudiante.carrera
        materias_carrera = Materia.objects.filter(carrera=carrera_alumno)
        return carrera_alumno, materias_carrera

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.estudiante.role  == 'student':
            if self._check_survey_existence(request.user):
                return render(request, self.survey_not_available_template)

            carrera_alumno, materias_carrera = self._get_user_career_and_subjects(request.user)

            form = EncuestaForm()
            context = {'form': form, 'materias': materias_carrera}
            return render(request, self.template_name, context)
        else:
            return redirect('usuarios:login_user')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.estudiante.role == 'student':
            encuesta_existente = Encuesta.objects.filter(usuario=request.user).exists()

            if encuesta_existente:
                return render(request, self.survey_not_available_template)

            form = EncuestaForm(request.POST)

            if form.is_valid():
                form.instance.usuario = request.user  # Asignar el usuario actual
                form.save()  # El formulario ahora maneja las respuestas y la encuesta

                messages.success(request, self.success_message)
                return redirect('encuesta:encuesta_confirmacion')

            context = {'form': form, 'materias': self._get_user_career_and_subjects(request.user)[1]}
            return render(request, self.template_name, context)
        else:
            return redirect('usuarios:login_user')

# 



class EncuestaConfirmacionAlumno(View):
    template_name = 'components/surveys/redirect_page_students.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class EncuestaConfirmacion(View):
    template_name = 'components/surveys/thank_you_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    

# class ConsultarRespuestasDocenteView(View):
#     template_name = 'components/surveys/consult_answers.html'

#     def get(self, request, *args, **kwargs):
#         # Verifica que el usuario actual sea un docente
#         if request.user.is_authenticated and request.user.role == 'teacher':
#             # Obtén las encuestas de los alumnos
#             encuestas_alumnos = EncuestaAlumno.objects.all()

#             # Imprime las respuestas en la consola del servidor para depurar
#             for encuesta in encuestas_alumnos:
#                 print(f"Alumno: {encuesta.alumno.username}, Materia: {encuesta.materia.nombre}")
#                 for respuesta in encuesta.obtener_respuestas_alumno():
#                     print(f"Pregunta: {respuesta['pregunta']}, Respuesta: {respuesta['respuesta']}")

#             # Pasa las encuestas al contexto
#             context = {'encuestas_alumnos': encuestas_alumnos}
#             return render(request, self.template_name, context)
#         else:
#             # Redirige a la página de inicio de sesión si el usuario no es un docente
#             return redirect('usuarios:login_user')
