from django.urls import path
from .views import CareersListView

app_name = "career"  # Cambiado a "career"

urlpatterns = [
    path('carreras/', CareersListView.as_view(), name="careers_list"),
]
