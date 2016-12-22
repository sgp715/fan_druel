import pandas as pd


def _get_stats_dataframe():

    url = 'http://www.basketball-reference.com/leagues/NBA_2017_per_game.html'

    player_stats = pd.read_html(url)[0]

    sd = {'Player': player_stats['Player'],
        'Pos': player_stats['Pos'],
        'Age': pd.to_numeric(player_stats['Age'], errors='coerce'),
        'G': pd.to_numeric(player_stats['G'], errors='coerce'),
        'GS': pd.to_numeric(player_stats['GS'], errors='coerce'),
        'MP': pd.to_numeric(player_stats['MP'], errors='coerce'),
        'FG%': pd.to_numeric(player_stats['FG%'], errors='coerce'),
        '3P%': pd.to_numeric(player_stats['3P%'], errors='coerce'),
        '2P%': pd.to_numeric(player_stats['2PA'], errors='coerce'),
        'eFG%': pd.to_numeric(player_stats['eFG%'], errors='coerce'),
        'FT%': pd.to_numeric(player_stats['FT'], errors='coerce'),
        'ORB': pd.to_numeric(player_stats['ORB'], errors='coerce'),
        'DRB': pd.to_numeric(player_stats['DRB'], errors='coerce'),
        'TRB': pd.to_numeric(player_stats['TRB'], errors='coerce'),
        'AST': pd.to_numeric(player_stats['AST'], errors='coerce'),
        'STL': pd.to_numeric(player_stats['STL'], errors='coerce'),
        'BLK': pd.to_numeric(player_stats['BLK'], errors='coerce'),
        'TOV': pd.to_numeric(player_stats['TOV'], errors='coerce'),
        'PF': pd.to_numeric(player_stats['PF'], errors='coerce'),
        'PS/G': pd.to_numeric(player_stats['PS/G'], errors='coerce')
    }

    return pd.DataFrame(sd)


def _generate_player_dataframe(players):

    pdf = pd.DataFrame(players, columns=['Player', 'Salary'])
    pdf['Salary'] = pd.to_numeric(pdf['Salary'], errors='coerce')
    return pdf


def play_dataframe(players):

    sdf = _get_stats_dataframe()
    pdf = _generate_player_dataframe(players)
    return pd.merge(sdf, pdf, on='Player')
