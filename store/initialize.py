import sqlite3
import pandas as pd
import numpy as np

# last table on pages
season = pd.read_html('stats/season.html')[26]
day1 = pd.read_html('stats/day1.html')[20]
day2 = pd.read_html('stats/day2.html')[20]
daily = day1.append(day2)

daily['FDP'] = (pd.to_numeric(daily['TRB'], errors='coerce') * 1.2) + \
               (pd.to_numeric(daily['AST'], errors='coerce') * 1.5) + \
               (pd.to_numeric(daily['STL'], errors='coerce') * 2.0) + \
               (pd.to_numeric(daily['BLK'], errors='coerce') * 2.0) + \
               (pd.to_numeric(daily['TOV'], errors='coerce') * -1.0) + \
               (pd.to_numeric(daily['PTS'], errors='coerce') * 1.0)

d = { 'FDP': daily['FDP'], 'Player': daily['Player'] }
fantasy = pd.DataFrame(d)

sd = {'Player': season['Player'],
      'Pos': season['Pos'],
      'Age': pd.to_numeric(season['Age'], errors='coerce'),
      'G': pd.to_numeric(season['G'], errors='coerce'),
      'GS': pd.to_numeric(season['GS'], errors='coerce'),
      'MP': pd.to_numeric(season['MP'], errors='coerce'),
      'FG%': pd.to_numeric(season['FG%'], errors='coerce'),
      '3P%': pd.to_numeric(season['3P%'], errors='coerce'),
      '2P%': pd.to_numeric(season['2PA'], errors='coerce'),
      'eFG%': pd.to_numeric(season['eFG%'], errors='coerce'),
      'FT%': pd.to_numeric(season['FT'], errors='coerce'),
      'ORB': pd.to_numeric(season['ORB'], errors='coerce'),
      'DRB': pd.to_numeric(season['DRB'], errors='coerce'),
      'TRB': pd.to_numeric(season['TRB'], errors='coerce'),
      'AST': pd.to_numeric(season['AST'], errors='coerce'),
      'STL': pd.to_numeric(season['STL'], errors='coerce'),
      'BLK': pd.to_numeric(season['BLK'], errors='coerce'),
      'TOV': pd.to_numeric(season['TOV'], errors='coerce'),
      'PF': pd.to_numeric(season['PF'], errors='coerce'),
      'PS/G': pd.to_numeric(season['PS/G'], errors='coerce')
      }

stat_data = pd.DataFrame(sd)

stats = pd.merge(stat_data, fantasy, on='Player')

conn = sqlite3.connect('database.db')

stats.to_sql('stats', conn)

conn.commit()
conn.close()
