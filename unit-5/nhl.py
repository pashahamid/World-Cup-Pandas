import requests
import json

class NhlTeams:
    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
        self.nhl_stats = response['teams']
    def get_team_names(self):
        res = []
        for team in self.nhl_stats:
            res.append(team['name'])
        return res
    def conferences(self):
        res = {}
        for team in self.nhl_stats:
            if team['conference']['name'] in res:
                res[team['conference']['name']] += 1
            else:
                res[team['conference']['name']] = 1
        return res
    def show_one(self):
        print(json.dumps(self.nhl_stats[0], indent=3))
t = NhlTeams()
#t.show_one()
print(t.conferences())