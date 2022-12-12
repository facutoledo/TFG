from datetime import datetime
from crum import get_current_user
from django.db import models
from django.urls import reverse
from Autenticacion.models import Usuario
from django.core import serializers


class BaseAuditoria(models.Model):
    borrado = models.BooleanField(default=False)
    creado_fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    creado_usuario = models.CharField(max_length=50, null=True, blank=True)
    modificado_fecha = models.DateTimeField(auto_now=True, null=True, blank=True)
    modificado_usuario = models.CharField(max_length=50, null=True, blank=True)
    borrado_fecha = models.DateTimeField(null=True, blank=True)
    borrado_usuario = models.CharField(max_length=50, null=True, blank=True)

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
    modificaciones = models.TextField(default = '', verbose_name='MODIFICACIONES')

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
                self.modificaciones = '\n' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '\n' + datos_anteriores_jason

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