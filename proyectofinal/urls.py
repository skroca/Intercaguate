from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as roca
from . import views

urlpatterns = [
        url(r'^admin/$', admin.site.urls),

 	url(r'^login/$', roca.login, name='Login'),
    url(r'^$', views.inicio, name = "Inicio"),
    url(r'^Inicio/$', views.inicio, name = "Inicio"),
 	url(r'^logout/$', roca.logout,{'next_page':'/'}, name='Logout'),
	url(r'^registro/$', views.registro, name ="Registro"),
    url(r'^(?P<id>\d+)/', views.detalle, name ="detail"),
    url(r'^editar/(?P<pk>\d+)/', views.editar, name ="detalle"),
    url(r'^imagen/nuevo/$', views.imagen_nuevo, name ="imagen_nuevo"),
    url(r'^eliminar/(?P<id>\d+)/', views.borrar, name ="eliminar"),
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
