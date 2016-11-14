from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from . import views

urlpatterns = [
        #url(r'^$', views.login, name = "Login"),
 	#url(r'^registro/', views.registro, name = "Registro"),
 	#url(r'^lista/', views.lista, name='Menu'),
 	#url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
