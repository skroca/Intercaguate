from django.shortcuts import render, get_object_or_404, redirect
from .models import Imagen
from .models import Comentarios
from .forms import ImagenForm
from .forms import ComentarioForm
from .forms import Login
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


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
	if request.user.is_authenticated():
		info = { "titulo": "IntercaGuate",  "object_list":queryset_list}
	else:
		info = { "titulo": "Inicie sesión para continuar"}
	return render(request,"index.html", info)



		



