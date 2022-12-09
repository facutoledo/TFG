from datetime import datetime
from django.forms import Form, CharField, EmailField, PasswordInput
from django.contrib.auth.forms import SetPasswordForm


class RegistroForm(Form):
    """
    dni
    correo_electrónico
    """
    dni = CharField()
    correo_electronico = EmailField()
    #contrasenia = CharField(widget=PasswordInput)


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

