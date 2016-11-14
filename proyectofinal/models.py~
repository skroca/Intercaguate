from django.db import models
from django.utils import timezone
from django.conf import settings


def upload_location(instance,filename):
	return "%s/%s" %(instance.id, filename,)

class Imagen(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	titulo = models.CharField(max_length =50)
	fecha_pub = models.DateTimeField(auto_now=False, auto_now_add= False)
	img = models.ImageField(upload_to=upload_location,null=True,blank=True,width_field="width_field",
	height_field= "height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	
	def __unicode__(self):
	    return self.titulo

	def __str__(self):
	    return self.titulo
	
	def __unicode__(self):
	    return self.usuario

	
	
	

class Comentarios(models.Model):
	id_comentario = models.ForeignKey(Imagen)
	comentario = models.TextField()
	fec = models.DateTimeField(default=timezone.now)
	fec_mod = models.DateTimeField(auto_now=True, auto_now_add= False)
	def __unicode__(self):
	    return self.comentario

	def __str__(self):
	    return self.comentario
	
	
       
