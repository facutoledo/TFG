from django.forms import Form, CharField, EmailField, PasswordInput


class RegistroForm(Form):
    """
    dni
    correo_electrónico
    """
    dni = CharField()
    correo_electronico = EmailField()
    contrasenia = CharField(widget=PasswordInput)
