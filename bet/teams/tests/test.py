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
        gen = [[1, 2], [1, 3], [2, 3]]
        positions = nba.generate_combos(list, 2)
        self.assertListEqual(gen, positions)

    def test__min_index(self):
        list = [0]
        min_i = nba._min_index(list)
        self.assertEqual(0, min_i)

        list = [1, 0, 2]
        min_i = nba._min_index(list)
        self.assertEqual(1, min_i)

        list = [9, 1, 2, 3, 4, 5, 6, 7, 8, 0]
        min_i = nba._min_index(list)
        self.assertEqual(9, min_i)

    def test__top_n(self):


        n = 10
        players = [ ['0'], ['0'], ['0'], ['0'], ['0'], ['0'], ['0'], ['0'], ['0'], ['0'],
                 ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1']]
        expected_top_n = [['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1'], ['1']]
        top_ten  = nba._top_n(n, players, 0)
        self.assertListEqual(expected_top_n, top_ten)

        players = [ ['0'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10']]
        expected_top_n = [ ['10'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']]
        top_ten  = nba._top_n(n, players, 0)
        self.assertListEqual(expected_top_n, top_ten)

        players = [ ['5'], ['1'], ['2'], ['3'], ['4'], ['0'], ['6'], ['7'], ['8'], ['9'], ['10'], ['11']]
        expected_top_n = [ ['5'], ['11'], ['2'], ['3'], ['4'], ['10'], ['6'], ['7'], ['8'], ['9']]
        top_ten  = nba._top_n(n, players, 0)
        self.assertListEqual(expected_top_n, top_ten)

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

        salary_index = 7

        team = [['17161-66521', 'PG', 'Marcelo', '', 'Huertas', '5.600000108991351', '7', '3500', 'LAL@TOR', 'LAL', 'TOR', '', '', '', ''],
                ['17161-15843', 'PG', 'Trey', '', 'Burke', '7.084615267240084', '13', '3500', 'WAS@SA', 'WAS', 'SA', '', '', '', '']]
        self.assertFalse(nba.check_max_salary(team, salary_index))


        team = [['17161-66521', 'PG', 'Marcelo', '', 'Huertas', '5.600000108991351', '7', '3500', 'LAL@TOR', 'LAL', 'TOR', '', '', '', ''],
                ['17161-15843', 'PG', 'Trey', '', 'Burke', '7.084615267240084', '13', '60500', 'WAS@SA', 'WAS', 'SA', '', '', '', '']]
        self.assertTrue(nba.check_max_salary(team, salary_index))

    # def test_possible_teams(self):
    #     data = nba.load_nba_data('./tests/player_list.csv')
    #     pgt0 = (['PG0','','','','','','','10000'], ['PG0','','','','','','', '0'])
    #     pgt1 = (['PG1','','','','','','','60000'], ['PG1','','','','','','', '0'])
    #     sgt0 = (['SG0','','','','','','','60000'], ['SG0','','','','','','', '0'])
    #     sgt1 = (['SG1','','','','','','','10000'], ['SG1','','','','','','', '0'])
    #     sft0 = (['SF0','','','','','','','10000'], ['SF0','','','','','','', '0'])
    #     sft1 = (['SF1','','','','','','','60000'], ['SF1','','','','','','', '0'])
    #     pft0 = (['PF0','','','','','','','60000'], ['PF0','','','','','','', '0'])
    #     pft1 = (['PF1','','','','','','','10000'], ['PF1','','','','','','', '0'])
    #     ct0 = (['C0','','','','','','','10000'], ['C0','','','','','','', '0'])
    #     ct1 = (['C1','','','','','','','60000'], ['C1','','','','','','', '0'])
    #     smaller_data = {'labels': data['labels'], 'data': { 'PG': [pgt0, pgt1],
    #                                                       'SG': [sgt0, sgt1],
    #                                                       'SF': [sft0, sft1],
    #                                                       'PF': [pft0, pft1],
    #                                                       'C': [ct0, ct1] } }
    #     expected_teams = [[pgt0, sgt1, sft0, pft1, ct0]]
    #     actual_teams = nba.possible_teams(smaller_data)
    #     self.assertListEqual(expected_teams, actual_teams)

    def test_just_teams(self):

        team = [['17328-15996', 'PG', 'Jerian', '', 'Grant', '8.864705702837776', '17', '3500', 'MIL@CHI', 'CHI', 'MIL', '', '', '', ''],
                ['17328-58490', 'PG', 'Wade', '', 'Baldwin IV', '9.33499984741211', '20', '3500', 'SAC@MEM', 'MEM', 'SAC', '', '', '', ''],
                ['17328-58661', 'SG', 'Rashad', '', 'Vaughn', '7.325000127156575', '12', '3500', 'MIL@CHI', 'MIL', 'CHI', '', '', '', ''],
                ['17328-23097', 'SG', 'Tomas', '', 'Satoransky', '9.799999660915798', '18', '3500', 'DET@WAS', 'WAS', 'DET', '', '', '', ''],
                ['17328-67026', 'SF', 'Jaylen', '', 'Brown', '9.84', '25', '3500', 'CHA@BOS', 'BOS', 'CHA', '', '', '', ''],
                ['17328-23798', 'SF', 'Caris', '', 'LeVert', '9.800000190734863', '4', '3500', 'BKN@ORL', 'BKN', 'ORL', '', '', '', ''],
                ['17328-23920', 'PF', 'Anthony', '', 'Bennett', '9.982352761661305', '17', '3500', 'BKN@ORL', 'BKN', 'ORL', '', '', '', ''],
                ['17328-23823', 'PF', 'Willie', '', 'Cauley-Stein', '9.619047619047619', '21', '3900', 'SAC@MEM', 'SAC', 'MEM', '', '', '', ''],
                ['17328-12362', 'C', 'DeMarcus', '', 'Cousins', '49.37916564941406', '24', '11000', 'SAC@MEM', 'SAC', 'MEM', '', '', '', '']]

        names = ['Jerian Grant',
                 'Wade Baldwin IV',
                 'Rashad Vaughn',
                 'Tomas Satoransky',
                 'Jaylen Brown',
                 'Caris LeVert',
                 'Anthony Bennett',
                 'Willie Cauley-Stein',
                 'DeMarcus Cousins']
        actual = nba.just_names(2, 4, team)
        self.assertListEqual(names, actual)

if __name__ == '__main__':

    unittest.main()
