from datetime import datetime
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from dateutil.relativedelta import relativedelta
from django.contrib.auth.hashers import check_password
from django.db import models


class UsuarioAdministrador(BaseUserManager):

    def _crear_usuario(self, dni, correo_electronico, password, **otros_campos):

        otros_campos.setdefault('is_superuser', False)
        otros_campos.setdefault('is_staff', False)
        otros_campos.setdefault('es_paciente', False)
        otros_campos.setdefault('es_medico', False)
        otros_campos.setdefault('is_active', False)
        if not dni:
            raise ValueError('Debe ingresar su Número de DNI')
        if not correo_electronico:
            raise ValueError('Debe ingresar un correo electrónico válido. '
                             'Allí se le enviará el link para establecer una contraseña')

        email = self.normalize_email(correo_electronico)
        usuario = self.model(dni=dni,
                             correo_electronico=email,
                             **otros_campos)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, dni, correo_electronico, password, **otros_campos):

        otros_campos.setdefault('is_superuser', True)
        otros_campos.setdefault('is_staff', True)
        otros_campos.setdefault('es_paciente', True)
        otros_campos.setdefault('es_medico', True)
        otros_campos.setdefault('is_active', True)

        if otros_campos.get('is_superuser') is not True:
            raise ValueError(
                'El Administrador debe tener asignado is_superuser=True.')
        if otros_campos.get('is_staff') is not True:
            raise ValueError(
                'El Administrador debe tener asignado is_staff=True.')
        if otros_campos.get('is_active') is not True:
            raise ValueError(
                'El Administrador debe tener asignado is_active=True.')
        if otros_campos.get('es_paciente') is not True:
            raise ValueError(
                'El Administrador debe tener asignado es_paciente=True.')
        if otros_campos.get('es_medico') is not True:
            raise ValueError(
                'El Administrador debe tener asignado es_medico=True.')

        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def create_user(self, dni, correo_electronico, password, **otros_campos):
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def create_personal(self, dni, correo_electronico, password, **otros_campos):
        otros_campos.setdefault('is_staff', True)
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def create_medico(self, dni, correo_electronico, password, **otros_campos):
        otros_campos.setdefault('is_staff', True)
        otros_campos.setdefault('es_medico', True)
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def create_paciente(self, dni, correo_electronico, password, **otros_campos):
        otros_campos.setdefault('es_paciente', True)
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    dni = models.CharField(max_length=255, unique=True, verbose_name='DNI')
    correo_electronico = models.EmailField(verbose_name='Correo electrónico')
    intentos_fallidos_de_ingreso = models.IntegerField(default=7)
    is_active = models.BooleanField(default=False, verbose_name="Usuario activo")
    fecha_ultimo_cambio_de_contrasena = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False, verbose_name="Usuario personal")
    es_paciente = models.BooleanField(default=False, verbose_name="Usuario paciente")
    es_medico = models.BooleanField(default=False, verbose_name="Usuario médico")
    objects = UsuarioAdministrador()

    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'dni'
    EMAIL_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['correo_electronico']

    _contrasena = None

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    def puede_ingresar(self):
        if self.is_active:
            _fecha_cambio_contrasena = self.fecha_ultimo_cambio_de_contrasena.date() + relativedelta(months=+6)

            if self.intentos_fallidos_de_ingreso == 0:
                self.is_active = False
            elif _fecha_cambio_contrasena < datetime.now():
                self.is_active = False
            self.save()

        return self.is_active

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.

        descuenta las veces que el usuario puso mal la contraseña
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        validado = check_password(raw_password, self.password, setter)

        if not validado:
            self.intentos_fallidos_de_ingreso = self.intentos_fallidos_de_ingreso - 1
        else:
            self.intentos_fallidos_de_ingreso = 7
        self.save()


        return validado

# #TODO Establecer el cambio de contraseña vía email
    # def save(self, *args, **kwargs):
    #     if self._contrasena is not None:
    #         password_validation.password_changed(self._contrasena, self)
    #         self.is_active = True
    #         #self._contrasena = None
    #     super(Usuario, self).save(*args, **kwargs)



