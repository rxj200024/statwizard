from django.urls import path
from .views import get_players

urlpatterns = [
    path('', get_players, name='get_players'),
]