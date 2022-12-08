from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(admin.ModelAdmin):
    search_fields = ('dni', 'correo_electronico',)
    list_filter = ('is_staff', 'es_paciente', 'es_medico', 'is_active',)
    ordering = ('dni',)
    list_display = ('dni', 'correo_electronico', 'is_staff', 'es_paciente', 'es_medico', 'is_active')

admin.site.register(Usuario, UserAdminConfig)
