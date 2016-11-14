from django.conf.urls import url
from . import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    #url(r'^$', views.lista_peliculas),
    url(r'^nueva/$', views.pelicula_nueva, name='pelicula_nueva'),
    ]
