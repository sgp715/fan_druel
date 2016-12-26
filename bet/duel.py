import pandas as pd
import numpy as np
from sklearn import preprocessing
import random


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


def label_players(clf, players):

    df = play_dataframe(players)
    if df.shape[0] == 0:
        print "Couldn't find players"
        return None
    df.dropna(inplace=True)
    X = np.array(df.drop(['Player', 'Salary', 'Pos'], axis=1))
    # X = preprocessing.scale(X)
    df['PFDP'] = clf.predict(X)

    return df


def max_player(df):

    index = df['PFDP'].idxmax()
    #player = df.loc[index]

    return index

def max_n_at_pos(df, n, pos):

    ps = []
    for i in range(n):
        index = max_player(df.loc[df['Pos'] ==  pos])
        player = df.loc[index]
        ps.append([player['Player'], player['Pos'], player['Salary'], player['PFDP']])
        df.drop(index, inplace=True)

    return ps

def assemble(df):

    pgs = max_n_at_pos(df, 2, 'PG')
    sgs = max_n_at_pos(df, 2, 'SG')
    pfs = max_n_at_pos(df, 2, 'SF')
    sfs = max_n_at_pos(df, 2, 'PF')
    c = max_n_at_pos(df, 1, 'C')

    team = pgs + sgs + pfs + sfs + c

    tdf = pd.DataFrame(team, columns=['Player', 'Pos','Salary','PFDP'])
    cost = tdf['Salary'].sum()
    while cost > 60000:

        new_index = df['PFDP'].idxmax()
        new_player_data =  df.loc[new_index]
        df.drop(new_index, inplace=True)

        pos = new_player_data['Pos']
        old_index = tdf.loc[tdf['Pos'] ==  pos]['Salary'].idxmax()
        tdf.drop(old_index, inplace=True)

        new_player = [new_player_data['Player'], new_player_data['Pos'], new_player_data['Salary'], new_player_data['PFDP']]
        pdf = pd.DataFrame([new_player], columns=['Player', 'Pos','Salary','PFDP'])
        tdf = tdf.append(pdf, ignore_index=True)


        cost = tdf['Salary'].sum()

    print tdf

    team_dict = tdf.to_dict()

    best_team = {"team": team_dict['Player'].values(),
                 "pos": team_dict['Pos'].values(),
                 "pfdp": team_dict['PFDP'].values()}

    return best_team
