from datetime import datetime
from crum import get_current_user
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from Autenticacion.models import Usuario
from django.core import serializers


class BaseAuditoria(models.Model):
    borrado = models.BooleanField(default=False)
    creado_fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    creado_usuario = models.CharField(max_length=50, null=True, blank=True)
    modificado_fecha = models.DateTimeField(null=True, blank=True)
    modificado_usuario = models.CharField(max_length=50, null=True, blank=True)
    borrado_fecha = models.DateTimeField(null=True, blank=True)
    borrado_usuario = models.CharField(max_length=50, null=True, blank=True)
    modificaciones = models.TextField(default = '', verbose_name='MODIFICACIONES')


    class Meta:
        abstract = True

class Paciente(BaseAuditoria):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    dni = models.CharField(max_length=50, unique=True, verbose_name='DNI')
    apellido = models.CharField(max_length=150, verbose_name='APELLIDO')
    nombre = models.CharField(max_length=150, verbose_name='NOMBRE')
    fecha_de_nacimiento = models.DateField(verbose_name='NACIMIENTO')
    correo_electronico = models.EmailField(verbose_name='CORREO_ELECTRONICO')
    pais = models.CharField(max_length=50, verbose_name='PAIS')
    provincia = models.CharField(max_length=50, verbose_name='PROVINCIA')
    localidad = models.CharField(max_length=50, verbose_name='LOCALIDAD')
    direccion = models.CharField(max_length=50, verbose_name='DIRECCION')
    telefono = models.CharField(max_length=50, verbose_name='TELEFONO')
    contacto = models.CharField(max_length=150, verbose_name='CONTACTO')
    antecedentes = models.TextField(null=True, default="")

    def __str__(self):
        return str(self.apellido) + ', ' + str(self.nombre)

    def save(self, *args, **kwargs):
        usuario = get_current_user()
        if usuario is not None:
            if not Paciente.objects.filter(dni=self.dni).exists():
                #registro la creación
                self.creado_fecha = datetime.now()
                self.creado_usuario = usuario.dni
            else:
                #Guardo los datos previos a la modificación. 
                datos_anteriores_jason = serializers.serialize('json', Paciente.objects.filter(pk=self.pk))
                self.modificaciones = 'version anterior - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n' + datos_anteriores_jason

                #registro la modificación o eliminación lógica
                if self.borrado:
                    self.borrado_fecha = datetime.now()
                    self.borrado_usuario = usuario.dni
                else:
                    self.modificado_fecha = datetime.now()
                    self.modificado_usuario = usuario.dni    
        super(Paciente, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pacientes')

class Medico(BaseAuditoria):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    dni = models.CharField(max_length=50, unique=True, verbose_name='DNI')
    apellido = models.CharField(max_length=150, verbose_name='APELLIDO')
    nombre = models.CharField(max_length=150, verbose_name='NOMBRE')
    correo_electronico = models.EmailField(verbose_name='CORREO_ELECTRONICO')
    telefono = models.CharField(max_length=50, verbose_name='TELEFONO')
    matricula = models.CharField(max_length=50, verbose_name='MATRICULA_PROFESIONAL')

    def __str__(self):
            return str(self.apellido) + ', ' + str(self.nombre)

    def save(self, *args, **kwargs):
        usuario = get_current_user()
        if usuario is not None:
            if not Medico.objects.filter(dni=self.dni).exists():
                #registro la creación
                self.creado_fecha = datetime.now()
                self.creado_usuario = usuario.dni
            else:
                #Guardo los datos previos a la modificación. 
                datos_anteriores_jason = serializers.serialize('json', Medico.objects.filter(pk=self.pk))
                self.modificaciones = 'version anterior - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n' + datos_anteriores_jason

                #registro la modificación o eliminación lógica
                if self.borrado:
                    self.borrado_fecha = datetime.now()
                    self.borrado_usuario = usuario.dni
                else:
                    self.modificado_fecha = datetime.now()
                    self.modificado_usuario = usuario.dni    
        super(Medico, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pacientes')

class BaseTurno(BaseAuditoria):
    ESTADO = (
        ('AUSENTE', 'Ausente'),
        ('EN ESPERA', 'En espera'),
        ('ATENDIENDO', 'Atendiendo'),
        ('ATENDIDO', 'Atendido'),
    )

    fecha = models.DateField(null=False, blank=False, verbose_name='FECHA')
    hora = models.TimeField(null=False, blank=False, verbose_name='HORA')
    estado = models.CharField(max_length=50, null=False, blank=False, default='AUSENTE', verbose_name='ESTADO', choices=ESTADO)
    observaciones = models.TextField(null=True, blank=True, verbose_name='OBSERVACIONES')
    class Meta:
        abstract = True

class TurnoConsultorio(BaseTurno):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False, blank=False,
                            verbose_name='MEDICO', related_name='consultorio_medico_related')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False,
                            verbose_name='PACIENTE', related_name='consultorio_paciente_related')
    mediciones_realizadas = models.TextField(null=True, blank=True, verbose_name='MEDICIONES_REALIZADAS')
    motivo_consulta = models.TextField(null=True, blank=True, verbose_name='MOTIVO_CONSULTA')
    diagnostico = models.TextField(null=True, blank=True, verbose_name='DIAGNOSTICO')
    tratamiento = models.TextField(null=True, blank=True, verbose_name='TRATAMIENTO')
    
    def save(self, *args, **kwargs):
        usuario = get_current_user()
        if usuario is not None:
            if not TurnoConsultorio.objects.filter(fecha=self.fecha, hora=self.hora, medico=self.medico).exists():
                #registro la creación
                self.creado_fecha = datetime.now()
                self.creado_usuario = usuario.dni
            else:
                #Guardo los datos previos a la modificación. 
                datos_anteriores = TurnoConsultorio.objects.filter(fecha=self.fecha, hora=self.hora, medico=self.medico)
                datos_anteriores_jason = serializers.serialize('json', datos_anteriores)
                self.modificaciones = 'version anterior - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n' + datos_anteriores_jason

                #recupero el turno si es que fue borrado y se lo quiere volver a crear
                if datos_anteriores.borrado:
                    self.borrado = False

                #registro la modificación o eliminación lógica
                if self.borrado:
                    self.borrado_fecha = datetime.now()
                    self.borrado_usuario = usuario.dni
                else:
                    self.modificado_fecha = datetime.now()
                    self.modificado_usuario = usuario.dni    
        super(TurnoConsultorio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('turnos_consultorio')

class TurnoEstudio(BaseTurno):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False, blank=False,
                            verbose_name='MEDICO', related_name='estudio_medico_related')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False,
                            verbose_name='PACIENTE', related_name='estudio_paciente_related')
    nombre_estudio = models.TextField(null=True, blank=True, verbose_name='NOMBRE_ESTUDIO')
    ubicacion_archivo = models.TextField(null=True, blank=True, verbose_name='UBICACIÓN_ARCHIVO')
    hash_archivo = models.TextField(null=True, blank=True, verbose_name='HASH_ARCHIVO')
    
    def save(self, *args, **kwargs):
        usuario = get_current_user()
        if usuario is not None:
            if not TurnoEstudio.objects.filter(fecha=self.fecha, hora=self.hora, medico=self.medico).exists():
                #registro la creación
                self.creado_fecha = datetime.now()
                self.creado_usuario = usuario.dni
            else:
                #Guardo los datos previos a la modificación. 
                datos_anteriores = TurnoEstudio.objects.filter(fecha=self.fecha, hora=self.hora, medico=self.medico)
                datos_anteriores_jason = serializers.serialize('json', datos_anteriores)
                self.modificaciones = 'version anterior - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n' + datos_anteriores_jason

                #recupero el turno si es que fue borrado y se lo quiere volver a crear
                if datos_anteriores.borrado:
                    self.borrado = False

                #registro la modificación o eliminación lógica
                if self.borrado:
                    self.borrado_fecha = datetime.now()
                    self.borrado_usuario = usuario.dni
                else:                    
                    self.modificado_fecha = datetime.now()
                    self.modificado_usuario = usuario.dni    
        super(TurnoEstudio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('turnos_estudio')

class HistoriaClinica(BaseAuditoria):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False,
                            verbose_name='PACIENTE', related_name='HisClin_paciente_related')
    ubicacion_archivo = models.TextField(verbose_name='UBICACIÓN_ARCHIVO')
    hash_archivo = models.TextField(verbose_name='HASH_ARCHIVO')
    observaciones = models.TextField(null=True, blank=True, verbose_name='OBSERVACIONES')

    
    def save(self, *args, **kwargs):
        usuario = get_current_user()
        if usuario is not None:
            histCli = HistoriaClinica.objects.filter(pk=self.pk)
            if not histCli.exists():
                #registro la creación
                self.creado_fecha = datetime.now()
                self.creado_usuario = usuario.dni
            else:
                #Guardo los datos previos a la modificación. 
                datos_anteriores =  HistoriaClinica.objects.filter(fecha=self.fecha, hora=self.hora, medico=self.medico)
                datos_anteriores_jason = serializers.serialize('json', datos_anteriores)
                self.modificaciones = 'version anterior - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n' + datos_anteriores_jason

                #recupero el turno si es que fue borrado y se lo quiere volver a crear
                if datos_anteriores.borrado:
                    self.borrado = False
                
                #registro la modificación o eliminación lógica
                if self.borrado:
                    self.borrado_fecha = datetime.now()
                    self.borrado_usuario = usuario.dni
                else:
                    self.modificado_fecha = datetime.now()
                    self.modificado_usuario = usuario.dni    
        super(HistoriaClinica, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('pagina_principal_paciente', kwargs={'pk':self.Paciente.pk}))
