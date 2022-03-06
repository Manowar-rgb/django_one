from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bd


# Create your views here.

def index(request):
    bbs = Bd.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})
