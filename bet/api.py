import falcon
from wsgiref import simple_server
from teams import nba
import json


class bestTeam(object):

    def on_post(self, req, resp):

        resp.status = falcon.HTTP_200

        dummy_team = {"team": ["Me", "Claire", "Max", "Elena,", "Dad", "Mom", "Rochester", "Jeff", "Jim"] }
        resp.body = json.dumps(dummy_team)

app = falcon.API()
best = bestTeam()

app.add_route("/bestTeam", best)


if __name__ == "__main__":
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
