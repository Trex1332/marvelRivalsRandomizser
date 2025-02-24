from django.shortcuts import render

import random
from randoms.models import Hero

# Create your views here.
def index(request):
    return render(request, 'randoms/index.html')