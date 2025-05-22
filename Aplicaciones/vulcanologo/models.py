from django.db import models

# Create your models here.
class vulcanologo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    # para visualizar los datos de mejor manera 
    def __str__(self): 
        fila = "{0}:  {1}  {2} {3}"
        return fila.format(self.id, self.nombre, self.apellido, self.especialidad, self.email)