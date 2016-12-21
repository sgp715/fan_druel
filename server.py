import json
import csv
from flask import Flask, send_file, request, abort
import os

app = Flask(__name__, static_url_path='', static_folder='app/static')

@app.route('/')
def index():
    return send_file('app/static/index.html')

@app.route('/bestTeam', methods=['POST'])
def best():

    csvfile = request.get_json()['file']
    print csvfile

    players = csvfile.split('\n')
    print players

    p_n_s = []

    for p in players[1:]:
        player = p.split(",")
        name = player[2].strip('"') + ' ' + player[4].strip('"')
        salary = player[7].strip('"')
        p_n_s.append((name, salary))

    if players:
        return json.dumps({"team": ["got it"]})

    abort(404)


if __name__ == "__main__":

    if os.environ.get('PROD'):
        app.run(host='0.0.0.0', port=8080)
    else:
        app.run(debug=True)
