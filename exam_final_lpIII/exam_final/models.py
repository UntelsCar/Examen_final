from django.db import models

# Create your models here.
class Pena_Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_de_registro = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'