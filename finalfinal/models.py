from django.db import models
from django.conf import settings

class Usuario(models.Model):
        dpi = models.IntegerField(max_length = 13)
        nombre = models.TextField()
        def __str__(self):
            return self.nombre

class Libro(models.Model):
        isbn = models.CharField(max_length=13)
        #portada = models.ImageField()
        titulo = models.TextField()
        autor = models.TextField()
        año = models.IntegerField()
        prestamista = models.ForeignKey(Usuario,null=True, blank = True)
        fecha_prestamo = models.DateTimeField(null=True, blank = True)

        def __str__(self):
            return self.titulo
class Pais(models.Model):
        pais = models.TextField()
        def __str__(self):
            return self.pais

class Editorial(models.Model):

        editorial= models.TextField()
        def __str__(self):
            return self.editorial

        
