from django.shortcuts import render

import random
from .models import Hero

# Create your views here.
def index(request):
    random_hero()
    return render(request, 'randoms/index.html')

def random_hero(request):
    heroes =Hero.objects.all()
    context = {'heroes': random.choice(heroes)}
    return render(request, 'randoms/randhero.html', context)
    
