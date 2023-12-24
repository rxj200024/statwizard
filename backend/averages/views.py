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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AveragesSerializer


# Create your views here.
@api_view(['GET'])
@csrf_exempt
@require_GET
def get_averages(request, id):
  player_dict = players.get_active_players()
  print(id)
  
  player = [player for player in player_dict if player['id'] == id][0]
  id = player['id']
  
  print(id)
  gamelog_player = playergamelog.PlayerGameLog(player_id = player['id'], season = '2023')
  
  gamelog_player_df = gamelog_player.get_data_frames()
  
  length_of_df = len(gamelog_player_df[0])
  
  # calculate points average
  sum_of_pts = gamelog_player_df[0]['PTS'].sum()
  pts_avg = round(sum_of_pts / length_of_df, 1)
  
  # calculate rebounds average
  sum_of_reb = gamelog_player_df[0]['REB'].sum()
  reb_avg = round(sum_of_reb / length_of_df, 1)
  
  # calculate assists average
  sum_of_ast = gamelog_player_df[0]['AST'].sum()
  ast_avg = round(sum_of_ast / length_of_df, 1)
  
  # calculate steals average
  sum_of_stl = gamelog_player_df[0]['STL'].sum()
  stl_avg = round(sum_of_stl / length_of_df, 1)
  
  # calculate blocks average
  sum_of_blk = gamelog_player_df[0]['BLK'].sum()
  blk_avg = round(sum_of_blk / length_of_df, 1)
  
  # calculate turnovers average
  sum_of_tov = gamelog_player_df[0]['TOV'].sum()
  tov_avg = round(sum_of_tov / length_of_df, 1)
  
  # print(name)
  print(pts_avg)
  print(reb_avg)
  print(ast_avg)
  print(stl_avg)
  print(blk_avg)
  print(tov_avg)

  data = {
    'id': player['id'],
    'name': player['full_name'],
    'first': player['first_name'],
    'last': player['last_name'],
    'pts': pts_avg,
    'reb': reb_avg,
    'ast': ast_avg,
    'stl': stl_avg,
    'blk': blk_avg,
    'tov': tov_avg,
  }
  
  serializer = AveragesSerializer({
    **data,
  })
  print(serializer.data)
  return Response(serializer.data)

