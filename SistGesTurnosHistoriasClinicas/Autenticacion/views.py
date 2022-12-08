from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from .forms import RegistroForm


class RegistroPersonalViews(FormView):
    template_name = "registro_empleados.html"
    form_class = RegistroForm
    #TODO página de bienvenida
    success_url = ''

    def form_valid(self, form):
        #todo enviar correo de verificación y que redirija a la página de establecer contraseña
        form.send_email()
        return HttpResponseRedirect