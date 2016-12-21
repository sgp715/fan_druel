import pandas as pd


def get_stats_dataframe():

    url = 'http://www.basketball-reference.com/leagues/NBA_2017_per_game.html'

    player_stats = pd.read_html(url)[0]

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

    return pd.DataFrame(sd)


def generate_player_dataframe(players):

    pdf = pd.DataFrame(players,columns=['Player','Salary','Pos'])
    pdf['Salary'] = pd.to_numeric(season['Salary'], errors='coerce')
    return pdf


def play_dataframe(sdf, pdf):

    return pd.merge(sdf, pdf, on='Player')
