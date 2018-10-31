import json
from findMax import findMaxPoints
from player import Player

def getPoints(scoreboards, box_scores, players, weeks):
    """
    with open('scoreboards.json', 'r') as infile:
        scoreboards = json.loads(infile.read())

    with open('box_scores.json', 'r') as infile:
        box_scores = json.loads(infile.read())
    """

    for week in range(1,weeks):
        for match in range(len(scoreboards[str(week)]['scoreboard']['matchups'])):
            for team in range(2):
                try:
                    ps = box_scores[str(week)][str(match)]['boxscore']['teams'][team]['slots']
                except:
                    continue

                # check if team is on a bye if odd man league
                if box_scores[str(week)][str(match)]['boxscore']['scheduleItems'][0]['matchups'][0]['isBye'] == True:
                    id = box_scores[str(week)][str(match)]['boxscore']['teams'][team]['teamId']
                    players[id-1].scores.append(0)
                    players[id-1].maxs.append(0)
                    # If on a bye, just add zeros for that week
                    continue

                info = []
                # loop through players
                for k,p in enumerate(ps):
                    # players on bye/injured won't have this entry
                    try:
                        pts = p['currentPeriodRealStats']['appliedStatTotal']
                    except KeyError:
                        pts = 0

                    try:
                        name = p['player']['lastName']
                    except KeyError:
                        name = None

                    try:
                        slots = p['player']['eligibleSlotCategoryIds']
                    except KeyError:
                        slots = []

                    l = []
                    l.append(name)
                    l.append(pts)
                    l.append(slots)
                    info.append(l)

                maxPoints = findMaxPoints(info)
                id = box_scores[str(week)][str(match)]['boxscore']['teams'][team]['teamId']
                realPoints = box_scores[str(week)][str(match)]['boxscore']['teams'][team]['appliedActiveRealTotal']

                players[id-1].scores.append(realPoints)
                players[id-1].maxs.append(maxPoints)

    return players
