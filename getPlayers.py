import json
from player import Player

def getPlayers(scoreboards, box_scores, leagueSize):
    players = [0] * leagueSize
    """
    with open('scoreboards.json', 'r') as infile:
        scoreboards = json.loads(infile.read())

    with open('box_scores.json', 'r') as infile:
        box_scores = json.loads(infile.read())
    """
    for i in range(len(box_scores['1'])):
        if box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['isBye'] == False:
            name1   = box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['awayTeam']['teamAbbrev']
            id1     = box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['awayTeam']['teamId']
            name2   = box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['homeTeam']['teamAbbrev']
            id2     = box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['homeTeam']['teamId']
            players[id1-1] = Player(name1, id1, [], [])
            players[id2-1] = Player(name2, id2, [], [])
        else:
            name   = box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['homeTeam']['teamAbbrev']
            id     = box_scores['1'][str(i)]['boxscore']['scheduleItems'][0]['matchups'][0]['homeTeam']['teamId']
            players[id-1] = Player(name, id, [], [])

    return players
