from django.contrib.auth import views
from django.urls import path, reverse_lazy

from .forms import *
from .views import *

urlpatterns = [
     path('ingreso/', views.LoginView.as_view(template_name='ingreso.html', success_url=reverse_lazy('bienvenida')),
         name='ingreso'),
     path('salir/', views.LogoutView.as_view(template_name='salir.html'),
         name='salir'),
     path('registro/', RegistroPacientesViews.as_view(template_name="registro_pacientes.html"),
         name='registro_pacientes'),
     path('registro_personal/', RegistroPersonalViews.as_view(template_name="registro_empleados.html"),
         name='registro_personal'),
     
     #Reestablecer la contraseña del usuario logueado
     path('contrasena_cambio/', views.PasswordChangeView.as_view(template_name='contrasena_cambio_form.html',
                                                                success_url=reverse_lazy('activar_cambio_contraseña_completado')),
         name='contrasena_cambio'),

     #Reestablecer la contraseña del usuario vía correo electrónico
     path('activar_cambio_contraseña/', 
          ActivarUsuarioCambioContraseña.as_view(template_name="activar_cambio_contraseña.html", success_url=reverse_lazy('activar_cambio_contraseña_hecho')),
          name='activar_cambio_contraseña'),
     path('activar_cambio_contraseña/hecho/', 
          views.PasswordResetDoneView.as_view(template_name="activar_cambio_contraseña_hecho.html"),
          name='activar_cambio_contraseña_hecho'),
     path('activar_cambio_contraseña/<uidb64>/<token>/', 
          views.PasswordResetConfirmView.as_view(template_name="activar_cambio_contraseña_confirmacion.html", 
               form_class=EstablecerContraseñaForm, success_url=reverse_lazy('activar_cambio_contraseña_completado')),
          name='activar_cambio_contraseña_confirmacion'),
     path('activar_cambio_contraseña/completado/', 
          views.PasswordResetCompleteView.as_view(template_name="activar_cambio_contraseña_completado.html"),
          name='activar_cambio_contraseña_completado'),
]
