from django.db import models

# Create your models here.

class Edificio(models.Model):
    
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo_estudiante = models.CharField(max_length=30, \
            choices=opciones_tipo_estudiante) 

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

class Departamento(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
