from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class BienvenidaView(TemplateView):
    template_name = 'inicio.html'
    #
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Bienvenido')
