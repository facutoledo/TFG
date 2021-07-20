from django.contrib.auth.backends import ModelBackend

from .models import Usuario


class Backend(ModelBackend):

    def authenticate(self, username=None, password=None):

        if username is None or password is None:
            raise ValueError('Debe ingresar su Número de DNI y Contraseña para identificarse')
        else:
            if '@' in username:
                kwargs = {'correo_electronico': username}
            else:
                kwargs = {'dni': username}
            try:
                usuario = Usuario.objects.get(**kwargs)
                if usuario.puede_ingresar():
                    if usuario.check_password(password):
                        return usuario
                    else:
                        raise ValueError('Contraseña incorrecta. Le quedan % intentos',
                                         getattr(usuario, 'intentos_fallidos_de_ingreso', None))
                else:
                    raise ValueError('El usuario no se encuentra activo. '
                                     'Para activar el usuario seleccione no recuerdo mi contraseña.')

            except Usuario.DoesNotExist:
                raise ValueError('No se encontró el usuario ingresado')

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None