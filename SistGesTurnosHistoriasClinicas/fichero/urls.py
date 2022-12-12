from django.contrib.auth import views
from django.urls import path

from .views import *

urlpatterns = [
    path('paciente/', PacientesView.as_view(), name="pacientes"),
    path('paciente/agregar/', AgregarPacienteView.as_view(), name="agregar_pacientes"),
    path('paciente/<int:pk>/editar/', EditarPacienteView.as_view(), name="editar_paciente"),
    path('paciente/<int:pk>/borrar/', BorrarPacienteView.as_view(), name="borrar_paciente"),
]
    
    