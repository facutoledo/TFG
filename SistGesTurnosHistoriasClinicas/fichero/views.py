from calendar import calendar
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import *
from .filters import *
from .forms import *

#--> PACIENTES

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

#--> MEDICOS

class MedicosView(ListView):
    model = Medico
    template_name = 'medicos/medicos.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MedicosFiltro(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        word = MedicosFiltro(self.request.GET, queryset=qs)
        return word.qs

class AgregarMedicoView(CreateView):
    model = Medico
    form_class = AgregarMedicoForm
    template_name = 'medicos/perfil_medico.html'
    success_url = reverse_lazy('medicos')

    def get_initial(self):
        inicial = super(AgregarMedicoView, self).get_initial()
        if self.kwargs.get('dni') is not None:
            inicial['dni'] = self.kwargs.get('dni')
            inicial['correo_electronico'] = self.kwargs.get('correo_electronico')
        return inicial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dni'] = self.kwargs.get('dni')
        context['correo_electronico'] = self.kwargs.get('correo_electronico')
        return context

class EditarMedicoView(UpdateView):
    model = Medico
    form_class = AgregarMedicoForm
    template_name = 'medicos/perfil_medico.html'
    success_url = reverse_lazy('medicos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medico'] = get_object_or_404(Medico, pk=self.kwargs.get('pk'))
        return context

#--> TURNOS CONSULTORIO

class TurnoConsultorioView(ListView):
    model = TurnoConsultorio
    template_name = 'turnos/turnos.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha = self.request.GET.get('fecha_selecta', False)
        medico_selecto = self.request.GET.get('radio_medico_selecto', False)
       
        if fecha == "":
            fecha = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)

        context['medicos'] = Medico.objects.all()
        context['medico_selecto'] = int(medico_selecto)
        context['fecha_selecta'] = fecha

        return context

    