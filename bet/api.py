import falcon
from wsgiref import simple_server
from teams import nba
import json
import csv


class bestTeam(object):

    def on_options(self, req, resp):

        resp.status = falcon.HTTP_200
        resp.set_header("Access-Control-Allow-Origin","*")
        resp.set_header("Access-Control-Allow-Headers","X-Requested-With,content-type,Access-Control-Allow-Origin")

    def on_post(self, req, resp):

        try:
            data = ''
            while True:
                    chunk = req.stream.read(4096)
                    if not chunk:
                        break
                    data += chunk
            csvfile = json.loads(data)['file']
            players = csvfile.split('\n')
            p_n_s = []

            for p in players[1:]:
                player = p.split(",")
                name = player[2].strip('"') + ' ' + player[4].strip('"')
                salary = player[7].strip('"')
                p_n_s.append((name, salary))

            # generate team

            resp.status = falcon.HTTP_200
            resp.set_header("Content-Type", "application/json")
            resp.set_header("Access-Control-Allow-Origin","*")
            dummy_team = {"team": ["Just Me", "And you"] }
            resp.body = json.dumps(dummy_team)
        except:
            resp.status = falcon.HTTP_400


app = falcon.API()
best = bestTeam()

app.add_route("/bestTeam", best)


if __name__ == "__main__":
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
