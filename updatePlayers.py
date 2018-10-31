from player import Player

def updatePlayers(players):
    colors = ['cornflowerblue', 'coral', 'crimson', 'goldenrod', 'darkblue', 'green',
                'blue', 'darkred', 'salmon', 'sienna', 'slateblue', 'violet']

    for i, p in enumerate(players):
        players[i].checkByes()
        players[i].setAverages()
        players[i].setDiffs()
        players[i].setColor(colors[i])
        #players[i].printPlayer()

    return players
