from django.contrib.auth import views
from django.urls import path

from .views import *

urlpatterns = [
    path('paciente/', PacientesView.as_view(), name="pacientes"),
    path('paciente/agregar/', AgregarPacienteView.as_view(), name="agregar_pacientes"),
    path('paciente/<int:pk>/editar/', EditarPacienteView.as_view(), name="editar_paciente"),
    path('paciente/<int:pk>/borrar/', BorrarPacienteView.as_view(), name="borrar_paciente"),

    path('medico/', MedicosView.as_view(), name="medicos"),
    path('medico/agregar/', AgregarMedicoView.as_view(), name="agregar_medico"),
    path('medico/agregar/<str:dni>/<str:correo_electronico>/', AgregarMedicoView.as_view(), name="cargar_perfil_medico"),
    path('medico/<int:pk>/editar/', EditarMedicoView.as_view(), name="editar_medico"),

    path('turnos/', TurnoConsultorioView.as_view(), name='turnos')
]
    
    