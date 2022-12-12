from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import *
from .filters import *
from .forms import *

class PacientesView(ListView):
    model = Paciente
    template_name = 'pacientes/pacientes.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PacientesFiltro(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        word = PacientesFiltro(self.request.GET, queryset=qs)
        return word.qs

class AgregarPacienteView(CreateView):
    model = Paciente
    form_class = AgregarPacienteForm
    template_name = 'pacientes/agregar_paciente.html'
    success_url = reverse_lazy('pacientes')

class EditarPacienteView(UpdateView):
    model = Paciente
    form_class = AgregarPacienteForm
    template_name = 'pacientes/agregar_paciente.html'


class BorrarPacienteView(UpdateView):
    model = Paciente
    form_class = BorrarPacienteForm
    template_name = 'pacientes/agregar_paciente.html'