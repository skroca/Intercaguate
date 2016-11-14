from django.shortcuts import render, get_object_or_404, redirect
from .models import Us
from .models import Tw
from .forms import PostUser
from .forms import PostTwitt
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import Subir

@login_required

def upload_image_view(request):
    if request.method = 'POST':
        form = Subir(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
    else:
	form = Subir();
    return render_to_response('albums_upload.html',locals(),context_instance=RequestContext(request))

def home_view(request):
    return render_to_response('base.html')

