from utils import load
from itertools import combinations
import numpy as np

def load_nba_data(file_name):

    data = load.load_csv(file_name)
    injury_index = data['labels']['Injury Indicator']
    position_index = data['labels']['Position']
    fppg_index = data['labels']['FPPG']

    players = {}

    fppgs = []
    for p in data['data']:
        fppgs.append(float(p[fppg_index]))

    mean = np.mean(fppgs)
    var = np.var(fppgs)
    # print "mean"
    # print mean
    #
    # print len(data['data'])

    # remove injured players
    for p in data['data']:
        # maybe make if O?
        if p[injury_index] != '':
            continue
        print "fppg"
        print p[fppg_index]
        if p[fppg_index] < mean:
            print "fppg"
            continue
        if p[position_index] in players:
            players[p[position_index]].append(p)
        else:
            players[p[position_index]] = [p]

    return {'labels':data['labels'], 'data': players}

def generate_combos(players, choosing):

    return list(combinations(players, choosing))

def possible_positions(data):
    """
    creates all combinations of players at positions
    """

    pgs = generate_combos(data['data']['PG'], 2)
    sgs = generate_combos(data['data']['SG'], 2)
    sfs = generate_combos(data['data']['SF'], 2)
    pfs = generate_combos(data['data']['PF'], 2)
    cs = generate_combos(data['data']['C'], 1)

    new_data = {'labels': data['labels'], 'data': { 'PG': pgs,
                                                    'SG': sgs,
                                                    'SF': sfs,
                                                    'PF': pfs,
                                                    'C': cs } }

    return new_data

def check_max_salary(team, salary_index):
    """
    checks if the current teams break the salary cap and doesn't return any
    that do
    """

    new_team = []

    total_salary = 0
    for players in team:
        salary = int(players[0][salary_index]) + int(players[1][salary_index])
        total_salary += salary
        if total_salary > 60000:
            return True
            continue

    return False

def possible_teams(data):
    """
    generates a list of possible_teams to field
    """

    salary_index = data['labels']['Salary']

    pgs = data['data']['PG']
    sgs = data['data']['SG']
    sfs = data['data']['SF']
    pfs = data['data']['PF']
    cs =  data['data']['C']

    # print len(pgs)
    # print len(sgs)
    # print len(sfs)
    # print len(pfs)
    # print len(cs)

    teams = []
    for pg in pgs:
        #if check_max_salary([pg], salary_index):
        #    continue
        for sg in sgs:
            #if check_max_salary([pg, sg], salary_index):
            #    continue
            for sf in sfs:
                #if check_max_salary([pg, sg, sf], salary_index):
                #    continue
                for pf in pfs:
                    #if check_max_salary([pg, sg, sf, pf], salary_index):
                    #    continue
                    for c in cs:
                        #if check_max_salary([pg, sg, sf, pf, c], salary_index):
                        #    continue
                        teams.append([pg, sg, sf, pf, c])
                        print "Number teams: " + str(len(teams))

    return teams
