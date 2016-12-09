from utils import load
from itertools import combinations
#import numpy as np

def _min_index(list):

    i = 0
    min_val = list[0]
    min_i = i
    for v in list[1:]:

        i += 1

        if v < min_val:
            min_i = i
            min_val = v

    return min_i

def _top_ten(players, index):

    top = []
    vals = []
    for p in players[0:10]:

        val = p[index]
        vals.append(val)

        top.append(p)

    min_i = _min_index(vals)
    min_val = vals[min_i]

    for p in players[10:]:

        val = p[index]

        if val > min_val:

            top[min_i] = p
            vals[min_i] = val

            min_i = _min_index(vals)
            min_val = vals[min_i]

    return top

def load_nba_data(file_name):

    data = load.load_csv(file_name)
    injury_index = data['labels']['Injury Indicator']
    position_index = data['labels']['Position']
    fppg_index = data['labels']['FPPG']

    players = {}

    # remove injured players
    for p in data['data']:
        # maybe make if O?
        if p[injury_index] != '':
            continue
        if p[position_index] in players:
            players[p[position_index]].append(p)
        else:
            players[p[position_index]] = [p]

    players['PG'] = _top_ten(players['PG'], fppg_index)
    players['SG'] = _top_ten(players['SG'], fppg_index)
    players['SF'] = _top_ten(players['SF'], fppg_index)
    players['PF'] = _top_ten(players['PF'], fppg_index)
    players['C'] = _top_ten(players['C'], fppg_index)

    return {'labels':data['labels'], 'data': players}

def generate_combos(players, choosing):

    combos = [list(s) for s in combinations(players, choosing)]

    return combos

# def possible_positions(data):
#     """
#     creates all combinations of players at positions
#     """
#
#     pgs = generate_combos(data['data']['PG'], 2)
#     sgs = generate_combos(data['data']['SG'], 2)
#     sfs = generate_combos(data['data']['SF'], 2)
#     pfs = generate_combos(data['data']['PF'], 2)
#     cs = generate_combos(data['data']['C'], 1)
#
#     new_data = {'labels': data['labels'], 'data': { 'PG': pgs,
#                                                     'SG': sgs,
#                                                     'SF': sfs,
#                                                     'PF': pfs,
#                                                     'C': cs } }
#
#     return new_data

def check_max_salary(team, salary_index):
    """
    checks if the current teams break the salary cap and doesn't return any
    that do
    """

    new_team = []

    salary = 0
    for player in team:

        salary += int(player[salary_index])

        if salary > 60000:
            return True
            continue

    return False

def sum_team_score(team, index):

    score = 0.0

    for p in team:
        score += float(p[index])

    return score

def possible_teams(data):
    """
    generates a list of possible_teams to field
    """

    salary_index = data['labels']['Salary']
    fppg_index = data['labels']['FPPG']

    pgs = generate_combos(data['data']['PG'], 2)
    sgs = generate_combos(data['data']['SG'], 2)
    sfs = generate_combos(data['data']['SF'], 2)
    pfs = generate_combos(data['data']['PF'], 2)
    cs =  [ [c] for c in data['data']['C'] ]

    teams = []
    max_score = 0
    best_team = []
    count = 1
    for pg in pgs:
        for sg in sgs:
            for sf in sfs:
                for pf in pfs:
                    if check_max_salary(pg + sg + sf + pf, salary_index):
                        continue
                    for c in cs:
                        new_team = pg + sg + sf + pf + c
                        if check_max_salary(new_team, salary_index):
                            continue
                        #teams.append(new_team)
                        # print "Number teams: " + str(len(teams))
                        team_score = sum_team_score(new_team, fppg_index)
                        if team_score > max_score:
                            max_score = team_score
                            best_team = new_team
                        print count
                        count += 1

    return best_team
