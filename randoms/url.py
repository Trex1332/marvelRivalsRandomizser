from django.urls import path

from . import views
from .views import random_hero

app_name = 'randoms'

urlpatterns = [
    path('',views.index, name='index'),
    path('random-hero/', random_hero, name='random-hero'),
]