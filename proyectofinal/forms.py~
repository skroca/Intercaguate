from django import forms
from .models import Imagen
from .models import Comentarios

class ImagenForm(forms.ModelForm):

	class Meta:
		model = Imagen
		fields = ["img","titulo","usuario","descripcion",]

class ComentarioForm(forms.ModelForm):

	class Meta:

		model = Comentarios
		fields = ["comentario"]
