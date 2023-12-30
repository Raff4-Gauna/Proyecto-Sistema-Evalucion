# from django.shortcuts import render, redirect
# from django.views import View
# from apps.encuestas.models import Encuesta, RespuestaEncuesta
# from django.contrib.auth.mixins import LoginRequiredMixin

# class DocenteEncuestasView(LoginRequiredMixin, View):
#     template_name = 'components/teacher/query_teacher.html'

#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.role == 'teacher':
#             docente = request.user.docente
#             materias_a_cargo = docente.materias.all()

#             # Obtener el ID de la materia desde los parámetros de consulta
#             materia_id = request.GET.get('materia_id')

#             # Filtrar encuestas por materia si se proporciona un ID de materia
#             if materia_id:
#                 encuestas = Encuesta.objects.filter(materia__in=materias_a_cargo, materia__id=materia_id).order_by('-fecha')
#             else:
#                 # Si no se proporciona un ID de materia, obtener todas las encuestas para las materias del docente
#                 encuestas = Encuesta.objects.filter(materia__in=materias_a_cargo).order_by('-fecha')

#             # Inicializar una lista para almacenar todas las respuestas de encuestas
#             todas_respuestas = []

#             # Para cada encuesta, obtener las respuestas asociadas
#             for encuesta in encuestas:
#                 respuestas_encuesta = RespuestaEncuesta.objects.filter(encuesta=encuesta)
#                 todas_respuestas.extend(respuestas_encuesta)

#             context = {'encuestas': encuestas, 'preguntas_respuestas': todas_respuestas, 'materias_a_cargo': materias_a_cargo}
#             return render(request, self.template_name, context)
#         else:
#             return redirect('usuarios:login_user')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views import View
from apps.encuestas.models import Encuesta, RespuestaEncuesta
from django.contrib.auth.mixins import LoginRequiredMixin

class DocenteEncuestasView(LoginRequiredMixin, View):
    template_name = 'components/teacher/query_teacher.html'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.docente.role == 'teacher':
            docente = request.user.docente
            materias_a_cargo = docente.materias.all()

            # Obtener el ID de la materia desde los parámetros de consulta
            materia_id = request.GET.get('materia_id')

            # Filtrar encuestas por materia si se proporciona un ID de materia
            if materia_id:
                encuestas = Encuesta.objects.filter(materia__in=materias_a_cargo, materia__id=materia_id).order_by('-fecha')
            else:
                # Si no se proporciona un ID de materia, obtener todas las encuestas para las materias del docente
                encuestas = Encuesta.objects.filter(materia__in=materias_a_cargo).order_by('-fecha')

            # Inicializar una lista para almacenar todas las respuestas de encuestas
            todas_respuestas = []

            # Para cada encuesta, obtener las respuestas asociadas
            for encuesta in encuestas:
                respuestas_encuesta = RespuestaEncuesta.objects.filter(encuesta=encuesta)
                todas_respuestas.extend(respuestas_encuesta)

            # Agregar paginación
            paginator = Paginator(todas_respuestas, self.paginate_by)
            page_number = request.GET.get('page')

            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)

            context = {'encuestas': encuestas, 'preguntas_respuestas': page, 'materias_a_cargo': materias_a_cargo}
            return render(request, self.template_name, context)
        else:
            return redirect('usuarios:login_user')

