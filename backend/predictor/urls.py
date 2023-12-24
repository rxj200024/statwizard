from django.urls import path
from .views import predict_stats

urlpatterns = [
    path('nba/player/<int:id>/', predict_stats, name='predict_stats'),
]