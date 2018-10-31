from player import Player
from collectData import collectData
from getPlayers import getPlayers
from getPoints import getPoints
from updatePlayers import updatePlayers
from graphPlayers import graphPlayers
from graphWeeks import graphWeeks

leagueID = 0
seasonID = 2018
swid = ''
espn_s2 = ''
weeks = 1 # TODO fix weeks number
league_size = 12

def main():
    print('Collecting data')
    scoreboards, box_scores = collectData(leagueID, seasonID, weeks, swid, espn_s2)

    print('Updating players')
    players = getPlayers(scoreboards, box_scores, league_size)
    players = getPoints(scoreboards, box_scores, players, weeks)
    players = updatePlayers(players)

    print('Creating graphs')
    graphPlayers(players)
    graphWeeks(players, weeks, league_size)

if __name__ == '__main__':
    main()
