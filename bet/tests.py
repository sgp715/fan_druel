import unittest
import pickle
import duel

players = [["Anthony Davis", "11600"],
           ["DeMar DeRozan","8300"],
           ["James Harden", "11600"],
           ["Jimmy Butler", "8200"],
           ["DeMarcus Cousins", "11200"],
           ["Giannis Antetokounmpo","10600"],
           ["LeBron James","10000"],
           ["John Wall", "9700"],
           ["Chris Paul", "9500"],
           ["Nicolas Batum", "7500"],
           ["Trevor Ariza","5600"],
           ["Karl-Anthony Towns", "9200"],
           ["Damian Lillard", "9100"],
           ["Blake Griffin", "8800"],
           ["Kyle Lowry", "8700"],
           ["Kevin Love", "8400"]]

with open('../store/clf.pkl', 'rb') as f:
    clf = pickle.load(f)

df = duel.label_players(clf, players)

team = duel.assemble(df)

# write some actual tests
