from datetime import datetime
from django import forms
from django.forms import BooleanField, Form, CharField, EmailField, PasswordInput
from django.contrib.auth.forms import SetPasswordForm

from .models import *

class RegistroForm(Form):
    """
    dni
    correo_electrónico
    """
    dni = CharField()
    correo_electronico = EmailField()

class RegistroEmpleadoForm(Form):
    """
    dni
    correo_electrónico
    es_medico
    is_staff
    """
        
    dni= CharField()
    correo_electronico= EmailField()
    is_staff = BooleanField(initial=False, required=False)
    es_medico = BooleanField(initial=False, required=False)


class EstablecerContraseñaForm(SetPasswordForm):
    
    def save(self, *args, commit=True, **kwargs):
        user = super().save(*args, commit=False, **kwargs)
        user.is_active = True
        user.fecha_ultimo_cambio_de_contrasena = datetime.now()
        if commit:
            user.save()
        return user

class ActivarUsuarioCambioContraseñaForm(Form):
    correo_electronico = EmailField()

