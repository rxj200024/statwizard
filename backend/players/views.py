from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

# Create your views here.
@csrf_exempt
@require_GET
def get_players(request):
  player_dict = players.get_active_players()
  serialized_data = {"data": player_dict}
  return JsonResponse(serialized_data, safe=False)
