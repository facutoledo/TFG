from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UsuarioAdministrador(BaseUserManager):

    def _crear_usuario(self, dni, correo_electronico, password, **otros_campos):

        otros_campos.setdefault('is_superuser', False)
        otros_campos.setdefault('is_staff', False)
        otros_campos.setdefault('es_paciente', False)
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
        otros_campos.setdefault('is_active', True)

        if otros_campos.get('is_superuser') is not True:
            raise ValueError(
                'El Administrador debe tener asignado is_superuser=True.')
        if otros_campos.get('is_staff') is not True:
            raise ValueError(
                'El Administrador debe tener asignado is_staff=True.')
        if otros_campos.get('es_paciente') is not True:
            raise ValueError(
                'El Administrador debe tener asignado es_paciente=True.')
        if otros_campos.get('is_active') is not True:
            raise ValueError(
                'El Administrador debe tener asignado is_active=True.')

        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def create_user(self, dni, correo_electronico, password, **otros_campos):
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def crear_personal(self, dni, correo_electronico, password, **otros_campos):
        otros_campos.setdefault('is_staff', True)
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)

    def crear_paciente(self, dni, correo_electronico, password, **otros_campos):
        otros_campos.setdefault('es_paciente', True)
        return self._crear_usuario(dni, correo_electronico, password, **otros_campos)


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    dni = models.CharField(max_length=255, unique=True, verbose_name='DNI')

    correo_electronico = models.EmailField(verbose_name='Correo electrónico')
    fecha_ultimo_cambio_de_contrasena = models.DateTimeField(blank=True, null=True)
    intentos_fallidos_de_ingreso = models.IntegerField(default=7)

    is_staff = models.BooleanField(default=False, verbose_name="Usuario personal")
    es_paciente = models.BooleanField(default=False, verbose_name="Usuario paciente")
    is_active = models.BooleanField(default=False, verbose_name="Usuario activo")

    objects = UsuarioAdministrador()

    USERNAME_FIELD = 'dni'
    EMAIL_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['correo_electronico']

    _contrasena = None

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    def puede_ingresar(self):
        return True #self.is_active

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self._contrasena is not None:
    #         password_validation.password_changed(self._contrasena, self)
    #         self._contrasena = None
