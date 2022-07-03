from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home/index.html')


def shorten(request, encoded_url):
    return render(request, 'shorten/index.html')


def shorten_details(request, shorten_url):
    return render(request, 'shorten-details/index.html')


def redirect_shorten_url():
    return "WIP"
