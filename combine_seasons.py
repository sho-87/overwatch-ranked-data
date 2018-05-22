"""
Combine individual season data into a single dataset
"""

import numpy as np
import os
import pandas as pd
import sys

dir_data = os.path.join(os.path.dirname(sys.argv[0]), 'data')

# combine separate files into single dataframe
data_seasons = []

for season in os.listdir(dir_data):
    if season != 'all_seasons.csv':
        season_num = season.split('.')[0][6:]
        
        df = pd.read_csv(os.path.join(dir_data, season))
        df['season'] = int(season_num)
        df['No medals'] = np.nan
        
        data_seasons.append(df)

data_all = pd.concat(data_seasons, axis=0, ignore_index=True)

# count the number of each medal type
medal_cols = ['Elim_medal', 'Obj_kills_medal', 'Obj_time_medal',
              'Dmg_medal', 'Heal_medal']

df_medals = data_all[medal_cols]
medal_count = df_medals[df_medals.isnull().sum(axis=1) != 5].apply(pd.Series.value_counts, axis=1).fillna(0)
medal_count.rename(columns={'Gold': 'Gold medals',
                            'Silver': 'Silver medals',
                            'Bronze': 'Bronze medals',
                            'None': 'No medals'}, inplace=True)
    
data_all.update(medal_count)

# add game mode column
game_modes = {'Assault': ['Hanamura', 'Horizon Lunar Colony', 'Temple of Anubis', 'Volskaya Industries'],
              'Escort': ['Dorado', 'Junkertown', 'Rialto', 'Route 66', 'Watchpoint: Gibraltar'],
              'Assault/Escort': ['Blizzard World', 'Eichenwalde', 'Hollywood', "King's Row", 'Numbani'],
              'Control': ['Ilios', 'Lijiang Tower', 'Nepal', 'Oasis']}

game_modes = dict((v,k) for k in game_modes for v in game_modes[k])  # Invert

data_all['Mode'] = data_all['Map'].replace(game_modes)

# reorder, sort, and save
col_order = ['season', 'Game #', 'Start SR', 'End SR', 'SR Change', 
             'Team SR avg', 'Enemy SR avg', 'Team Stack', 'Enemy Stack', 
             'Role 1', 'Role 2', 'Result', 'Streak', 'Leaver', 
             'Map', 'Mode', 'Match Time',
             'Gold medals', 'Silver medals', 'Bronze medals', 'No medals',
             'Elim', 'Elim_career', 'Elim_medal', 
             'Obj_kills', 'Obj_kills_career', 'Obj_kills_medal', 
             'Obj_time', 'Obj_time_career', 'Obj_time_medal', 
             'Dmg', 'Dmg_career', 'Dmg_medal', 
             'Heal', 'Heal_career', 'Heal_medal', 
             'Death', 'Death_career']

data_all = data_all[col_order]
data_all = data_all.sort_values(['season', 'Game #'])
data_all.to_csv(os.path.join(dir_data, 'all_seasons.csv'), index=False)                   
