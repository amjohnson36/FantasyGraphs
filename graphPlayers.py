import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from player import Player
import os

def graphPlayers(players):
    if not os.path.exists('graphs'):
        os.makedirs('graphs')

    for player in players:
        # Plot each player's individual graph
        x = np.arange(1, len(player.scores)+1)

        scores = np.asarray(player.scores)
        diff = np.asarray(player.diff)
        plt.figure()

        p1 = plt.bar(x, scores, color = player.color)
        p2 = plt.bar(x, diff, bottom = scores, color = player.color, alpha = 0.4)

        plt.xlabel('Week')
        plt.ylabel('Points')
        plt.text(1, 195, 'Average Points: {0:.1f}\nAverage Max: {1:.1f}\nRatio: {2:.3f}'
            .format(player.avgscore, player.avgmax, player.avgscore/player.avgmax))
        plt.yticks(np.arange(0, 230, 25))
        plt.title('{}'.format(player.name))
        plt.legend((p1[0], p2[0]), ("Points","Max Potential Points"), loc=1)
        plt.savefig('graphs/{}.jpg'.format(player.name), dpi=300)
        plt.close()
