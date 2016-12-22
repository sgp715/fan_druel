import json
import csv
import os
import pickle
import sqlite3
from flask import Flask, send_file, request, abort, g


app = Flask(__name__, static_url_path='', static_folder='app/static')


DATABASE = 'store/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database(DATABASE)
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


CLF = 'store/clf.pkl'

def get_clf():
    clf = getattr(g, '_clf', None)
    if clf is None:
        with open(CLF,'rb') as pf:
            clf = g._clf = pickle.load(pf)
    return clf


@app.route('/')
def index():
    return send_file('app/static/index.html')

@app.route('/bestTeam', methods=['POST'])
def best():

    csvfile = request.get_json()['file']

    players = csvfile.split('\n')

    p_n_s = []

    for p in players[1:]:
        player = p.split(",")
        name = player[2].strip('"') + ' ' + player[4].strip('"')
        salary = player[7].strip('"')
        pos = player[1].strip('"')
        p_n_s.append([name, pos, salary])

    if players:
        return json.dumps({"team": ["got it"]})

    abort(404)


if __name__ == "__main__":

    if os.environ.get('PROD'):
        app.run(host='0.0.0.0', port=8080)
    else:
        app.run(debug=True)
