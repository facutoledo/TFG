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
        lista_turnos = None
        estado_selecto = self.request.GET.get('radio_estado_selecto', False)
        
        if estado_selecto is False:
            estado_selecto = 'TODOS'

        if fecha == "":
            fecha = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
        
        if medico_selecto is not False and fecha != "":
            lista_turnos = TurnoConsultorio.objects.filter(fecha=fecha, medico=int(medico_selecto))
            

        context['medicos'] = Medico.objects.all()
        context['medico_selecto'] = int(medico_selecto)
        context['fecha_selecta'] = fecha
        context['turnos'] = lista_turnos
        context['estado_selecto'] = estado_selecto

        return context

class AgregarTurnoConsultorioView(CreateView):
    model = TurnoConsultorio
    form_class = AgregarTurnoConsultorioForm
    template_name = 'turnos/agregar_turno_consultorio.html'
    success_url = reverse_lazy('turnos_consultorio')
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha_selecta = None
        fecha_selecta2 = None
        hora_selecta = None
        medico_selecto = None
        paciente_selecto = None
        paciente_dni = None
        paciente_apellido = None
        paciente_nombre = None
        siguiente = 'Cambiar'
        pacientes = None
        borrado = False
        refresh = self.request.GET.get('refresh', 0)
        
        if self.kwargs.get('pk') == None:
            context['nuevo_paciente'] = 'nuevo'
        else:
            context['nuevo_paciente'] = 'edito'

        if self.kwargs.get('pk') != None and refresh == 0:
            id_turno = self.kwargs.get('pk')
            turno = get_object_or_404(TurnoConsultorio, pk=id_turno)
            fecha_selecta = turno.fecha.strftime('%d-%m-%Y')
            fecha_selecta2 = turno.fecha.strftime('%Y-%m-%d')
            hora_selecta = turno.hora.strftime('%H:%M')
            medico_selecto = turno.medico.pk
            paciente_selecto = turno.paciente.pk
            paciente_dni = turno.paciente.dni
            paciente_apellido = turno.paciente.apellido
            paciente_nombre = turno.paciente.nombre     
            borrado = turno.borrado 
            refresh +=1            

        elif self.request.method == 'GET':
            fecha_selecta = self.request.GET.get('fecha', datetime.today().strftime('%d-%m-%Y'))
            fecha_selecta2 = self.request.GET.get('fecha', datetime.today().strftime('%Y-%m-%d'))
            hora_selecta = self.request.GET.get('hora', datetime.now().time().strftime('%H:%M'))
            medico_selecto = self.request.GET.get('medico', False)
            paciente_selecto = self.request.GET.get('paciente', None)
            paciente_dni = self.request.GET.get('paciente_dni', "")
            paciente_apellido = self.request.GET.get('paciente_apellido', "")
            paciente_nombre = self.request.GET.get('paciente_nombre', "")
            siguiente = self.request.GET.get('siguiente', 'Cambiar')
            borrado = self.request.GET.get('borrado', False)

            try:
                fecha_selecta = datetime.strptime(fecha_selecta, '%Y-%m-%d')
                fecha_selecta = fecha_selecta.strftime('%d-%m-%Y')
            except:
                print('error-formato-fechas')

            if borrado == 'on':
                borrado = True
        else:
            fecha_selecta = self.request.POST.get('fecha', datetime.today().strftime('%d-%m-%Y'))
            hora_selecta = self.request.POST.get('hora', datetime.now().time().strftime('%H:%M'))
            medico_selecto = self.request.POST.get('medico', False)
            paciente_selecto = self.request.POST.get('paciente', None)
            borrado = self.request.POST.get('borrado', False)


        if medico_selecto is False:
            medico_selecto = self.kwargs.get('medico', False)

        if paciente_selecto != None:
            paciente_selecto = int(paciente_selecto)
        
        if paciente_dni != None or paciente_apellido != None or paciente_nombre != None:
            pacientes = Paciente.objects.filter(borrado=False,
                                                dni__icontains=paciente_dni,
                                                apellido__icontains=paciente_apellido,
                                                nombre__icontains=paciente_nombre)[:10]

   
        context['medicos'] = Medico.objects.all()
        context['fecha_selecta'] = fecha_selecta
        context['fecha_selecta2'] = fecha_selecta2
        context['hora_selecta'] = hora_selecta
        context['medico_selecto'] = int(medico_selecto)
        context['paciente_selecto'] = paciente_selecto
        context['paciente_dni'] = paciente_dni
        context['paciente_apellido'] = paciente_apellido
        context['paciente_nombre'] = paciente_nombre
        context['pacientes'] = pacientes
        context['siguiente'] = siguiente
        context['borrado'] = borrado
        context['refresh'] = refresh

        return context    

class EditarTurnoConsultorioView(UpdateView):
    model = TurnoConsultorio
    form_class = BorrarTurnoConsultorioForm
    template_name = 'turnos/agregar_turno_consultorio.html'
    success_url = reverse_lazy('turnos_consultorio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha_selecta = None
        fecha_selecta2 = None
        hora_selecta = None
        medico_selecto = None
        paciente_selecto = None
        paciente_dni = None
        paciente_apellido = None
        paciente_nombre = None
        siguiente = 'Cambiar'
        pacientes = None
        borrado = False
        refresh = self.request.GET.get('refresh', 0)

        if self.kwargs.get('pk') != None and refresh == 0:
            id_turno = self.kwargs.get('pk')
            turno = get_object_or_404(TurnoConsultorio, pk=id_turno)
            fecha_selecta = turno.fecha.strftime('%d-%m-%Y')
            fecha_selecta2 = turno.fecha.strftime('%Y-%m-%d')
            hora_selecta = turno.hora.strftime('%H:%M')
            medico_selecto = turno.medico.pk
            paciente_selecto = turno.paciente.pk
            paciente_dni = turno.paciente.dni
            paciente_apellido = turno.paciente.apellido
            paciente_nombre = turno.paciente.nombre     
            borrado = turno.borrado 
            refresh +=1            

        elif self.request.method == 'GET':
            fecha_selecta = self.request.GET.get('fecha', datetime.today().strftime('%d-%m-%Y'))
            fecha_selecta2 = self.request.GET.get('fecha', datetime.today().strftime('%Y-%m-%d'))
            hora_selecta = self.request.GET.get('hora', datetime.now().time().strftime('%H:%M'))
            medico_selecto = self.request.GET.get('medico', False)
            paciente_selecto = self.request.GET.get('paciente', None)
            paciente_dni = self.request.GET.get('paciente_dni', "")
            paciente_apellido = self.request.GET.get('paciente_apellido', "")
            paciente_nombre = self.request.GET.get('paciente_nombre', "")
            siguiente = self.request.GET.get('siguiente', 'Cambiar')
            borrado = self.request.GET.get('borrado', False)

            try:
                fecha_selecta = datetime.strptime(fecha_selecta, '%Y-%m-%d')
                fecha_selecta = fecha_selecta.strftime('%d-%m-%Y')
            except:
                print('error-formato-fechas')

            if borrado == 'on':
                borrado = True
        else:
            fecha_selecta = self.request.POST.get('fecha', datetime.today().strftime('%d-%m-%Y'))
            hora_selecta = self.request.POST.get('hora', datetime.now().time().strftime('%H:%M'))
            medico_selecto = self.request.POST.get('medico', False)
            paciente_selecto = self.request.POST.get('paciente', None)
            borrado = self.request.POST.get('borrado', False)


        if medico_selecto is False:
            medico_selecto = self.kwargs.get('medico', False)

        if paciente_selecto != None:
            paciente_selecto = int(paciente_selecto)
        
        if paciente_dni != None or paciente_apellido != None or paciente_nombre != None:
            pacientes = Paciente.objects.filter(borrado=False,
                                                dni__icontains=paciente_dni,
                                                apellido__icontains=paciente_apellido,
                                                nombre__icontains=paciente_nombre)[:10]

   
        context['medicos'] = Medico.objects.all()
        context['fecha_selecta'] = fecha_selecta
        context['fecha_selecta2'] = fecha_selecta2
        context['hora_selecta'] = hora_selecta
        context['medico_selecto'] = int(medico_selecto)
        context['paciente_selecto'] = paciente_selecto
        context['paciente_dni'] = paciente_dni
        context['paciente_apellido'] = paciente_apellido
        context['paciente_nombre'] = paciente_nombre
        context['pacientes'] = pacientes
        context['siguiente'] = siguiente
        context['borrado'] = borrado
        context['refresh'] = refresh

        return context    
