from django.contrib import admin

# Register your models hefrom django.contrib import admin
from .models import Usuario
from .models import Libro
from .models import Pais
from .models import Editorial
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Pais)
admin.site.register(Editorial)
