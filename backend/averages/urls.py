from django.urls import path
from .views import get_averages

urlpatterns = [
    path('nba/player/<int:id>/', get_averages, name='get_averages'),

]