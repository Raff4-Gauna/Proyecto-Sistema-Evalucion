from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request, *args, **kwargs):
     
        
        return render(request, 'home.html')

def handling_404(request, exception):
    return render(request, '404/404.html', {})

