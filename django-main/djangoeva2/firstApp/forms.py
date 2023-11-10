from django import forms
from firstApp.models import Cliente

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        labels = {
            'nombre': 'Nombre',
            'apellido': 'apellido',
            'correo': 'correo',
            'Contraseña': 'Contraseña',
            'Rut': 'Rut',
            'Direccion': 'Direccion',
        }


        