from django.http import HttpResponse
from django.shortcuts import redirect, render

# from core.utils import *
from .models import *


def redir(request):
    return redirect('index')

def index(request):
    return render(request, 'core/index.html')

def pageNotFound(request, exception):
    data = {
        'title': '404',
    }
    return render(request, 'core/404.html', context=data)