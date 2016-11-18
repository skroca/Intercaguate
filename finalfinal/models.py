from django.db import models
from django.conf import settings

class Usuario(models.Model):
        dpi = models.IntegerField()
        nombre = models.TextField()
        def __str__(self):
            return self.nombre

class Pais(models.Model):
        pais = models.TextField()
        def __str__(self):
            return self.pais

class Editorial(models.Model):

        editorial= models.TextField()
        def __str__(self):
            return self.editorial

class Libro(models.Model):
        isbn = models.CharField(max_length=13)
        #portada = models.ImageField()
        titulo = models.TextField()
        autor = models.TextField()
        año = models.IntegerField()
        prestamista = models.ForeignKey(Usuario,null=True, blank = True)
        fecha_prestamo = models.DateTimeField(null=True, blank = True)
        pais = models.ForeignKey(Pais, null = True)
        editorial = models.ForeignKey(Editorial,null=True)
        def __str__(self):
            return self.titulo
