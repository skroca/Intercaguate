from django.shortcuts import render, get_object_or_404, redirect
from .models import Imagen
from .models import Comentarios
from .forms import ImagenForm, ImagenEditar
from .forms import ComentarioForm
from .forms import Login
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import F

def registro(request):
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():

			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			email = form.cleaned_data["email"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name
			user.is_staff = True
			user.is_superuser = True
			user.save()
			return HttpResponseRedirect(reverse('Login'))
	else:
		form = Login()

	info = { 'form': form,}
	return render(request,"registro.html",info)

def inicio(request):
	queryset_list = Imagen.objects.all().order_by("-fecha_pub")
	usuario = request.user
	if request.user.is_authenticated():
		info = { "titulo": "IntercaGuate",  "object_list":queryset_list, "us": usuario}
	else:
		info = { "titulo": "Inicie sesión para continuar"}
	return render(request,"index.html", info)

def detalle(request, id=None):
	instance = get_object_or_404(Imagen,id=id)

	instancia = Imagen.objects.all()

	#instance2 = get_object_or_404(Comentarios,id=id)
	queryset = Comentarios.objects.filter(id_comentario= instance.id)
	usuario = request.user
	imagenactual = instancia[instance.id-1]
	form = ComentarioForm(request.POST or None)
	info2 = {"lista":queryset,"titulo": instance.titulo, "instance": instance, "us":usuario,
	"form":form}
	if form.is_valid():
		instance = form.save(commit = False)
		#instance.user = request.user
		instance.id_comentario = imagenactual
		instance.save()
		#return render(request,"detalle.html",info2)
		return HttpResponseRedirect("/" + str(imagenactual.id) + "/")


	return render(request,"detalle.html",info2)

def editar(request, pk):
	edita = get_object_or_404(Imagen, pk=pk)
	ins = Imagen.objects.all()
	imagena= ins[edita.id -1]
	if request.method == "POST":
		form = ImagenEditar(request.POST, instance=edita)
		if form.is_valid():
			editar = form.save(commit=False)
			#editar.img = imagena.img
			editar.author = request.user
			editar.save()
			return redirect("/")
	else:
		form = ImagenEditar(instance=edita)
		infos ={"form": form,"edi":imagena}
	return render(request, 'editar.html', infos)


def imagen_nuevo(request):
	if request.method == "POST":
		form = ImagenForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			imagennuevo = form.save(commit=False)
			imagennuevo.usuario = request.user
			imagennuevo.fecha_pub = timezone.now()
			imagennuevo.save()
			return HttpResponseRedirect("/")
	else:
		form = ImagenForm()
	return render(request, 'Publicacion.html', {'form': form})
def borrar(request, id):
	borra = get_object_or_404(Comentarios,id=id)
	inss= Comentarios.objects.filter(pk=id)
	inss.delete()
	return redirect("/")
