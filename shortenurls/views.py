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
    def generateRoute():
        perm = list(permutations(characters, 3))
        choice = ''.join(random.choice(perm))
        print('possible shorten url: %s', choice)
        return choice

    def incrementRoute(route):
        routeChars = list(route)
        routeChars.reverse()
        newRouteChars = []
        index = 0
        while (index < len(routeChars)):
            char = routeChars[index]
            if char == '9':
                newRouteChars.append('a')
            elif char == 'z':
                newRouteChars.append('A')
            elif (char == 'Z') and (index == len(routeChars)-1):
                newRouteChars = ['0'] * len(routeChars)
                break
            elif char == 'Z':
                newRouteChars.append('0')
            else:
                newChar = bytes([bytes(char, 'utf-8')[0] + 1]).decode('utf-8')
                newRouteChars.append(newChar)
                newRouteChars += routeChars[index+1:len(routeChars)]
                newRouteChars.reverse()
                break
            index += 1
        return ''.join(newRouteChars)

    url = base64.b64decode(encoded_url).decode('utf-8')
    route = ''
    if len(URL.objects.all()) == len(list(permutations(characters, 3))):
        # DB is full
        oldEntry = URL.objects.order_by('created_at').first()
        route = oldEntry.shorten
        oldEntry.delete()
    else:
        # DB is not full
        route = generateRoute()
        db_result = URL.objects.filter(shorten=route)
        while len(db_result) != 0:
            # Find route that is not used
            route = incrementRoute(route)
            db_result = URL.objects.filter(shorten=route)
    new_url = URL(shorten=route, original=url,
                  created_at=timezone.now())
    new_url.save()
    context = {
        'shorten_url': route
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
