from django.shortcuts import render
from .models import Libro
from .forms import Ingreso
from django.shortcuts import redirect

# Create your views here.
def ingresar(request):
    if request.method == "POST":

        form = Ingreso(request.POST)
        if form.is_valid():
                post = form.save(commit=False)

                post.save()

                return redirect('finalfinal/ingreso.html', {'form': form})
    else:
            form = Ingreso()
    return render(request, 'finalfinal/ingreso.html', {'form': form})
