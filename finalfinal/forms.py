from django import forms
from .models import Libro

class Ingreso(forms.ModelForm):

        class Meta:
            model = Libro
            fields = ('isbn', 'titulo','autor','año','pais','editorial')
