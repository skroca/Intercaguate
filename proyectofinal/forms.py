from django import forms
from .models import Imagen
from .models import Comentarios
from django.contrib.auth.models import User
from django.forms import ModelForm

class Login(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name','last_name']
		widgets = { 'password': forms.PasswordInput(),}

class ImagenForm(forms.ModelForm):

	class Meta:
		model = Imagen
		fields = ["img","titulo","usuario","descripcion",]

class ComentarioForm(forms.ModelForm):

	class Meta:

		model = Comentarios
		fields = ["comentario"]


