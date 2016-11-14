from django.contrib import admin
from proyectofinal.models import Imagen
from proyectofinal.models import Comentarios


class PostImagen(admin.ModelAdmin):
    list_display= ["usuario","img","titulo","fecha_pub"]
    list_display_links= ["titulo"]
    list_filter= ["usuario"]
    search_fields= ["usuario","titulo"]
    class Meta:
        model = Imagen

class PostComentarios(admin.ModelAdmin):
    list_display= ["comentario","fec","fec_mod"]
    list_display_links= ["fec"]
    list_filter= ["fec"]
    list_editable=["comentario"]
    search_fields= ["comentario"]
    class Meta:
        model = Comentarios

admin.site.register(Imagen)
admin.site.register(Comentarios)
