import django_filters

from .models import *


class PacientesFiltro(django_filters.FilterSet):

    class Meta:
        model = Paciente
        fields = {
            'dni': {'icontains'},
            'apellido': {'icontains'},
            'nombre': {'icontains'},
        }

class MedicosFiltro(django_filters.FilterSet):

    class Meta:
        model = Medico
        fields = {
            'dni': {'icontains'},
            'apellido': {'icontains'},
            'nombre': {'icontains'},
        }

# class TurnoConsultorioFiltro(django_filters.filterset):
#     fecha = django_filters.DateFilter()
#     hora = django_filters.TimeFilter()
#     author = django_filters.ModelChoiceFilter(queryset=Medico.objects.all())

#     class Meta:
#         model = TurnoConsultorio
#         fields = [
#             'fecha',
#             'hora',
#             'medico',
#         ]
