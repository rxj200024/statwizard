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
def predict_stats(request, id):
  # career = playercareerstats.PlayerCareerStats(player_id=player_id)
  player_dict = players.get_active_players()
  
  player = [player for player in player_dict if player['id'] == id][0]
  id = player['id']
  
  gamelog_player = playergamelog.PlayerGameLog(player_id = player['id'], season = '2023')
  
  gamelog_player_df = gamelog_player.get_data_frames()
  
  # linear regression prediction based off the last ten games
  
  # points
  X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
  y = np.array([gamelog_player_df[0]['PTS'][0],
                gamelog_player_df[0]['PTS'][1],
                gamelog_player_df[0]['PTS'][2], 
                gamelog_player_df[0]['PTS'][3],
                gamelog_player_df[0]['PTS'][4],
                gamelog_player_df[0]['PTS'][5],
                gamelog_player_df[0]['PTS'][6],
                gamelog_player_df[0]['PTS'][7],
                gamelog_player_df[0]['PTS'][8],
                gamelog_player_df[0]['PTS'][9]])
  
  model = LinearRegression()
  model.fit(X,y)
  
  next_data_item = np.array([[11]])
  
  pts = model.predict(next_data_item)
  pts = abs(round(pts[0], 1))
  
  # rebounds
  X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
  y = np.array([gamelog_player_df[0]['REB'][0],
                gamelog_player_df[0]['REB'][1],
                gamelog_player_df[0]['REB'][2], 
                gamelog_player_df[0]['REB'][3],
                gamelog_player_df[0]['REB'][4],
                gamelog_player_df[0]['REB'][5],
                gamelog_player_df[0]['REB'][6],
                gamelog_player_df[0]['REB'][7],
                gamelog_player_df[0]['REB'][8],
                gamelog_player_df[0]['REB'][9]])
  
  model = LinearRegression()
  model.fit(X,y)
  
  next_data_item = np.array([[11]])
  
  reb = model.predict(next_data_item)
  reb = abs(round(reb[0], 1))
  
  # assists
  X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
  y = np.array([gamelog_player_df[0]['AST'][0],
                gamelog_player_df[0]['AST'][1],
                gamelog_player_df[0]['AST'][2], 
                gamelog_player_df[0]['AST'][3],
                gamelog_player_df[0]['AST'][4],
                gamelog_player_df[0]['AST'][5],
                gamelog_player_df[0]['AST'][6],
                gamelog_player_df[0]['AST'][7],
                gamelog_player_df[0]['AST'][8],
                gamelog_player_df[0]['AST'][9]])
  
  model = LinearRegression()
  model.fit(X,y)
  
  next_data_item = np.array([[11]])
  
  ast = model.predict(next_data_item)
  ast = abs(round(ast[0], 1))
  
  # steals
  X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
  y = np.array([gamelog_player_df[0]['STL'][0],
                gamelog_player_df[0]['STL'][1],
                gamelog_player_df[0]['STL'][2], 
                gamelog_player_df[0]['STL'][3],
                gamelog_player_df[0]['STL'][4],
                gamelog_player_df[0]['STL'][5],
                gamelog_player_df[0]['STL'][6],
                gamelog_player_df[0]['STL'][7],
                gamelog_player_df[0]['STL'][8],
                gamelog_player_df[0]['STL'][9]])
  
  model = LinearRegression()
  model.fit(X,y)
  
  next_data_item = np.array([[11]])
  
  stl = model.predict(next_data_item)
  stl = abs(round(stl[0], 1))
  
  # blocks
  X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
  y = np.array([gamelog_player_df[0]['BLK'][0],
                gamelog_player_df[0]['BLK'][1],
                gamelog_player_df[0]['BLK'][2], 
                gamelog_player_df[0]['BLK'][3],
                gamelog_player_df[0]['BLK'][4],
                gamelog_player_df[0]['BLK'][5],
                gamelog_player_df[0]['BLK'][6],
                gamelog_player_df[0]['BLK'][7],
                gamelog_player_df[0]['BLK'][8],
                gamelog_player_df[0]['BLK'][9]])
  
  model = LinearRegression()
  model.fit(X,y)
  
  next_data_item = np.array([[11]])
  
  blk = model.predict(next_data_item)
  blk = abs(round(blk[0], 1))
  
  # turnovers
  X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
  y = np.array([gamelog_player_df[0]['TOV'][0],
                gamelog_player_df[0]['TOV'][1],
                gamelog_player_df[0]['TOV'][2], 
                gamelog_player_df[0]['TOV'][3],
                gamelog_player_df[0]['TOV'][4],
                gamelog_player_df[0]['TOV'][5],
                gamelog_player_df[0]['TOV'][6],
                gamelog_player_df[0]['TOV'][7],
                gamelog_player_df[0]['TOV'][8],
                gamelog_player_df[0]['TOV'][9]])
  
  model = LinearRegression()
  model.fit(X,y)
  
  next_data_item = np.array([[11]])
  
  tov = model.predict(next_data_item)
  tov = abs(round(tov[0], 1))
  
  print(f'Points: {pts}')
  print(f'Rebounds: {reb}')
  print(f'Assists: {ast}')
  print(f'Steals: {stl}')
  print(f'Blocks: {blk}')
  print(f'Turnovers: {tov}')
  
  data = {
    'id': player['id'],
    'name': player['full_name'],
    'pts': pts,
    'reb': reb,
    'ast': ast,
    'stl': stl,
    'blk': blk,
    'tov': tov,
  }
  

  return JsonResponse(data)

  
  
  
  
  
  

