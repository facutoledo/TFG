from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .models import Usuario

from .forms import *

class RegistroPersonalViews(FormView):
    template_name = "registro_empleados.html"
    form_class = RegistroForm
    #TODO página de bienvenida

    def form_valid(self, form):
        #todo enviar correo de verificación y que redirija a la página de establecer contraseña
        context = super().get_context_data() #{'fieldValues': self.request.POST}        
        dni = self.request.POST['dni']
        correo_electronico = self.request.POST['correo_electronico']
        

        if not Usuario.objects.filter(dni=dni).exists():
            #if not Usuario.objects.filter(correo_electronico=correo_electronico).exists():
            
            #Creo el usuario sin contraseña e inactivo. luego tendrá que activarlo desde el correo electrónico
            usuario = Usuario.objects.create_user(dni=dni, correo_electronico=correo_electronico, password='contraseña')
            usuario.is_active=False
            usuario.save()

            #Armo y envío el correo electrónico
            dominio = '127.0.0.1:8000' #self.get_current_site(self.request).domain
            
            uid =  urlsafe_base64_encode(force_bytes(usuario.pk)),
            token = PasswordResetTokenGenerator().make_token(usuario),
            
            link = reverse('activar_cambio_contraseña_confirmacion', kwargs={'uidb64': uid[0], 'token': token[0]})

            url_activacion = 'http://'+dominio+link

            email_cuerpo = 'Hola, para activar tu cuenta hacé click en el link a continuación y seguí los pasos que te indican \n' + url_activacion
            email_asunto = "Activa tu cuenta"

            email = EmailMessage(
                    email_asunto,
                    email_cuerpo,
                    settings.EMAIL_HOST_USER,
                    [correo_electronico],
                )
            email.send(fail_silently=False)
            
            messages.success(self.request, 'Account successfully created')
            return render(self.request, 'activar_cambio_contraseña_hecho.html')
            
            # else:
            #     messages.error(self.request, 'el DNI '+ dni + ' ya se encuentra registrado')
            #     return render(self.request, 'registro_empleados.html', context)
        else:
            messages.error(self.request, 'el DNI '+ dni + ' ya se encuentra registrado')
            return render(self.request, 'registro_empleados.html', context)

        
        form.send_email()
        return HttpResponseRedirect

class ActivarUsuarioCambioContraseña(FormView):
    template_name = "activar_cambio_contraseña.html"
    success_url = reverse_lazy('activar_cambio_contraseña_hecho')
    form_class = ActivarUsuarioCambioContraseñaForm

    def form_valid(self, form):
        context = super().get_context_data() 
        correo_electronico = self.request.POST['correo_electronico']
        
        print(correo_electronico)

        if Usuario.objects.filter(correo_electronico=correo_electronico).exists():
            
            usuario = Usuario.objects.filter(correo_electronico=correo_electronico).first()
            print(usuario.pk)

            #Armo y envío el correo electrónico
            dominio = '127.0.0.1:8000' #self.get_current_site(self.request).domain
            
            uid =  urlsafe_base64_encode(force_bytes(usuario.pk)),
            token = PasswordResetTokenGenerator().make_token(usuario),
            
            link = reverse('activar_cambio_contraseña_confirmacion', kwargs={'uidb64': uid[0], 'token': token[0]})

            url_activacion = 'http://'+dominio+link

            email_cuerpo = 'Hola, para activar tu cuenta hacé click en el link a continuación y seguí los pasos que te indican \n' + url_activacion
            email_asunto = "Activa tu cuenta"

            email = EmailMessage(
                    email_asunto,
                    email_cuerpo,
                    settings.EMAIL_HOST_USER,
                    [correo_electronico],
                )
            email.send(fail_silently=False)
            
            messages.success(self.request, 'Account successfully created')
            return render(self.request, 'activar_cambio_contraseña_hecho.html')
            
            # else:
            #     messages.error(self.request, 'el DNI '+ dni + ' ya se encuentra registrado')
            #     return render(self.request, 'registro_empleados.html', context)
        else:
            messages.error(self.request, 'el DNI '+ dni + ' ya se encuentra registrado')
            return render(self.request, 'registro_empleados.html', context)

        
        form.send_email()
        return HttpResponseRedirect