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

