from django.shortcuts import render
from django.views.generic import View
from .models import Carrera

# Create your views here.
class CareersListView(View):
    def get(self, request, *args, **kwargs):
        careers = Carrera.objects.all()
        context={
            'careers': careers
        }
        return render(request, 'components/careers/careers_list.html', context)