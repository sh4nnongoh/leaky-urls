from django.shortcuts import render, redirect
from django.http import HttpResponse
import base64
import random
from itertools import permutations
from .models import URL
from django.utils import timezone

# Create your views here.
characters = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]


def home(request):
    return render(request, 'home/index.html')


def shorten(request, encoded_url):
    url = base64.b64decode(encoded_url).decode('utf-8')
    print('url: %s', url)
    perm = list(permutations(characters, 3))
    choice = ''.join(random.choice(perm))
    print('possible shorten url: %s', choice)
    db_result = URL.objects.filter(shorten=choice)
    print('db result: %s', db_result)
    if len(db_result) == 0:
        new_url = URL(shorten=choice, original=url,
                      created_at=timezone.now())
        new_url.save()
        print('new url saved')
        context = {
            'shorten_url': choice
        }

    return render(request, 'shorten/index.html', context)


def shorten_details(request, shorten_url):
    route = shorten_url
    db_result = URL.objects.filter(shorten=route)
    if len(db_result) == 0:
        return redirect('/')
    entry = db_result.first()
    context = {
        'original': entry.original,
        'shorten_url': entry.shorten,
        'created_at': entry.created_at,
    }
    return render(request, 'shorten-details/index.html', context)


def redirect_shorten_url(request, shorten_url):
    route = shorten_url.split('/')[-1]
    db_result = URL.objects.filter(shorten=route)
    if len(db_result) == 0:
        return redirect('/')
    return redirect(db_result.first().original)
