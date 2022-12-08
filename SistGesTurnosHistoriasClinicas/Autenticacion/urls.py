from django.contrib.auth import views
from django.urls import path, reverse_lazy

from .views import *

urlpatterns = [
    path('ingreso/', views.LoginView.as_view(template_name='ingreso.html', success_url=reverse_lazy('bienvenida')),
         name='ingreso'),
    path('salir/', views.LogoutView.as_view(template_name='salir.html'),
         name='salir'),

    path('contrasena_cambio/hecho/', views.PasswordChangeDoneView.as_view(template_name='contrasena_cambio_hecho.html'),
         name='contrasena_cambio_hecho'),
    path('contrasena_cambio/', views.PasswordChangeView.as_view(template_name='contrasena_cambio_form.html',
                                                                success_url=reverse_lazy('contrasena_cambio_hecho')),
         name='contrasena_cambio'),

    #las siguientes 4 direcciones son para reestablecer la contraseña del usuario vía correo electrónico
    path('password_reset/', views.PasswordResetView.as_view(template_name="password_reset_form.html"),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name='password_reset_complete'),


    path('registro_personal/', RegistroPersonalViews.as_view(template_name="registro_empleados.html"),
         name='registro_personal'),
]
