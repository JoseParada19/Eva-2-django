from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=25)
    contrasena = models.CharField(max_length=30)
    rut = models.CharField(max_length=15)
    direccion = models.CharField(max_length=70)
  

  
    def __str__(self) -> str:
        return self.nombre



