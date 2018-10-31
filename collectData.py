import requests
import json

def collectData(leagueID, seasonID, weeks, swid, espn_s2):
    scoreboards = {}
    box_scores = {}

    for week in range(1, weeks):
        scoreboard = requests.get('http://games.espn.com/ffl/api/v2/scoreboard',
                        params={'leagueId': leagueID, 'seasonId': seasonID, 'matchupPeriodId': week},
                        cookies={'swid': swid, 'espn_s2': espn_s2})
        scoreboard = scoreboard.json()
        scoreboards[week] = scoreboard

        box_scores[week] = {}
        # loop through matchups that week
        for match in range(len(scoreboard['scoreboard']['matchups'])):
            homeID = scoreboard['scoreboard']['matchups'][match]['teams'][0]['team']['teamId']
            r = requests.get('http://games.espn.com/ffl/api/v2/boxscore',
                             params={'leagueId': leagueID, 'seasonId': seasonID,
                                     'teamId': homeID, 'matchupPeriodId': week},
                             cookies={'SWID': swid, 'espn_s2': espn_s2}
                            )
            r = r.json()
            box_scores[week][match] = r

    with open('scoreboards.json', 'w') as outfile:
        json.dump(scoreboards, outfile)

    with open('box_scores.json', 'w') as outfile:
        json.dump(box_scores, outfile)

    with open('scoreboards.json', 'r') as infile:
        json_scoreboards = json.loads(infile.read())

    with open('box_scores.json', 'r') as infile:
        json_box_scores = json.loads(infile.read())

    return json_scoreboards, json_box_scores
