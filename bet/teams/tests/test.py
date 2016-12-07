# execute from parent directory

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import utils
import nba
import unittest

class Tests(unittest.TestCase):

    def test_generate_combos(self):
        list = [1, 2, 3]
        gen = [(1, 2), (1, 3), (2, 3)]
        positions = nba.generate_combos(list, 2)
        self.assertListEqual(gen, positions)

    # def test_possible_positions(self):
    #     data = nba.load_nba_data('./tests/player_list.csv')
    #     pg0 = ['PG0']
    #     pg1 = ['PG1']
    #     sg0 = ['SG0']
    #     sg1 = ['SG1']
    #     sf0 = ['SF0']
    #     sf1 = ['SF1']
    #     pf0 = ['PF0']
    #     pf1 = ['PF1']
    #     c0 = ['C0']
    #     c1 = ['C1']
    #     smaller_data = {'labels': data['labels'], 'data': { 'PG': [pg0, pg1],
    #                                                         'SG': [sg0, sg1],
    #                                                         'SF': [sf0, sf1],
    #                                                         'PF': [pf0, pf1],
    #                                                         'C': [c0, c1] } }
    #     expected_data = {'labels': data['labels'], 'data': { 'PG': [(pg0, pg1)],
    #                                                         'SG': [(sg0, sg1)],
    #                                                         'SF': [(sf0, sf1)],
    #                                                         'PF': [(pf0, pf1)],
    #                                                         'C': [(c0, c1)] } }

    def test_check_max_salary(self):

        fake_team_low = [(['0'], ['0'])]
        actual_team_low = nba.check_max_salary(fake_team_low, 0)
        self.assertFalse(actual_team_low)

        fake_team_high = [(['60001'], ['0'])]
        actual_team_high = nba.check_max_salary(fake_team_high, 0)
        self.assertTrue(actual_team_high)

        fake_team_low = [(['0'], ['0']), (['60000'], ['0'])]
        actual_team_low = nba.check_max_salary(fake_team_low, 0)
        self.assertFalse(actual_team_low)

        fake_team_low = [(['20000'], ['0']), (['20000'], ['0']), (['20000'], ['0'])]
        actual_team_low = nba.check_max_salary(fake_team_low, 0)
        self.assertFalse(actual_team_low)

        fake_team_high = [(['20001'], ['0']), (['20000'], ['0']), (['20000'], ['0'])]
        actual_team_high = nba.check_max_salary(fake_team_high, 0)
        self.assertTrue(actual_team_high)
        fake_team_high = [(['20000'], ['0']), (['20001'], ['0']), (['20000'], ['0'])]
        actual_team_high = nba.check_max_salary(fake_team_high, 0)
        self.assertTrue(actual_team_high)
        fake_team_high = [(['20000'], ['0']), (['20000'], ['0']), (['0'], ['20001'])]
        actual_team_high = nba.check_max_salary(fake_team_high, 0)
        self.assertTrue(actual_team_high)

    def test_possible_teams(self):
        data = nba.load_nba_data('./tests/player_list.csv')
        pgt0 = (['PG0','','','','','','','10000'], ['PG0','','','','','','', '0'])
        pgt1 = (['PG1','','','','','','','60000'], ['PG1','','','','','','', '0'])
        sgt0 = (['SG0','','','','','','','60000'], ['SG0','','','','','','', '0'])
        sgt1 = (['SG1','','','','','','','10000'], ['SG1','','','','','','', '0'])
        sft0 = (['SF0','','','','','','','10000'], ['SF0','','','','','','', '0'])
        sft1 = (['SF1','','','','','','','60000'], ['SF1','','','','','','', '0'])
        pft0 = (['PF0','','','','','','','60000'], ['PF0','','','','','','', '0'])
        pft1 = (['PF1','','','','','','','10000'], ['PF1','','','','','','', '0'])
        ct0 = (['C0','','','','','','','10000'], ['C0','','','','','','', '0'])
        ct1 = (['C1','','','','','','','60000'], ['C1','','','','','','', '0'])
        smaller_data = {'labels': data['labels'], 'data': { 'PG': [pgt0, pgt1],
                                                          'SG': [sgt0, sgt1],
                                                          'SF': [sft0, sft1],
                                                          'PF': [pft0, pft1],
                                                          'C': [ct0, ct1] } }
        expected_teams = [[pgt0, sgt1, sft0, pft1, ct0]]
        actual_teams = nba.possible_teams(smaller_data)
        self.assertListEqual(expected_teams, actual_teams)

if __name__ == '__main__':

    unittest.main()
