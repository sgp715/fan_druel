import falcon
from wsgiref import simple_server
from teams import nba
import json


class bestTeam(object):

    def on_post(self, req, resp):

        try:
            data = ''
            while True:
                    chunk = req.stream.read(4096)
                    if not chunk:
                        break
                    data += chunk
                    print data
            dummy_team = {"team": [['17328-15996', 'PG', 'Jerian', '', 'Grant', '8.864705702837776', '17', '3500', 'MIL@CHI', 'CHI', 'MIL', '', '', '', ''], ['17328-58490', 'PG', 'Wade', '', 'Baldwin IV', '9.33499984741211', '20', '3500', 'SAC@MEM', 'MEM', 'SAC', '', '', '', ''], ['17328-58661', 'SG', 'Rashad', '', 'Vaughn', '7.325000127156575', '12', '3500', 'MIL@CHI', 'MIL', 'CHI', '', '', '', ''], ['17328-23097', 'SG', 'Tomas', '', 'Satoransky', '9.799999660915798', '18', '3500', 'DET@WAS', 'WAS', 'DET', '', '', '', ''], ['17328-67026', 'SF', 'Jaylen', '', 'Brown', '9.84', '25', '3500', 'CHA@BOS', 'BOS', 'CHA', '', '', '', ''], ['17328-23798', 'SF', 'Caris', '', 'LeVert', '9.800000190734863', '4', '3500', 'BKN@ORL', 'BKN', 'ORL', '', '', '', ''], ['17328-23920', 'PF', 'Anthony', '', 'Bennett', '9.982352761661305', '17', '3500', 'BKN@ORL', 'BKN', 'ORL', '', '', '', ''], ['17328-23823', 'PF', 'Willie', '', 'Cauley-Stein', '9.619047619047619', '21', '3900', 'SAC@MEM', 'SAC', 'MEM', '', '', '', ''], ['17328-12362', 'C', 'DeMarcus', '', 'Cousins', '49.37916564941406', '24', '11000', 'SAC@MEM', 'SAC', 'MEM', '', '', '', '']] }
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(dummy_team)
        except:
            resp.status = falcon.HTTP_400


app = falcon.API()
best = bestTeam()

app.add_route("/bestTeam", best)


if __name__ == "__main__":
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
