from django import forms

from .models import *

#--> PACIENTES

class AgregarPacienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AgregarPacienteForm, self).__init__(*args, **kwargs)
        self.fields['contacto'].required = False

    class Meta:
        model = Paciente
        fields = ('dni', 'apellido', 'nombre', 'fecha_de_nacimiento',
                  'pais', 'provincia', 'localidad', 'direccion',
                  'telefono', 'contacto', )

        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI (solo numeros)'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido/s'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre/s'}),
            'fecha_de_nacimiento': forms.DateInput(format='%d/%m/%Y',
                                          attrs={'class': 'form-control', 'placeholder': 'Naciemiento (dd/mm/aaaa)'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control',}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'value': 'Argentina'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'value': 'Chaco'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'value': 'Resistencia'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Teléfono'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Datos del Contacto: Nom., Ape. y Tel.'}),
            
        }

class BorrarPacienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BorrarPacienteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Paciente
        fields = ('dni', 'apellido', 'nombre', 'fecha_de_nacimiento',
                  'pais', 'provincia', 'localidad', 'direccion',
                  'telefono', 'contacto', 'borrado')

        widgets = {
            'dni': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'fecha_de_nacimiento': forms.DateInput(format='%d/%m/%Y',
                                          attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={ 'readonly': 'readonly', 'class': 'form-control',}),
            'pais': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'provincia': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }

#--> MEDICOS

class AgregarMedicoForm(forms.ModelForm):
    
    class Meta:
        model = Medico
        fields = ('dni', 'apellido', 'nombre', 'correo_electronico',
                  'telefono', 'matricula', )

        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI (solo numeros)'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido/s'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre/s'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control',}),
            'telefono': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Teléfono'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Número de matrícula'}),
            
        }

#--> TURNOS


