import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from player import Player
import os

def graphWeeks(players, weeks, leagueSize):
    if not os.path.exists('graphs'):
        os.makedirs('graphs')

    index = np.arange(leagueSize)
    n = [player.name for player in players]

    for week in range(weeks-1):
        plt.figure()
        fig, ax = plt.subplots()
        for i, player in enumerate(players):
            ax.bar(i, player.scores[week], color = player.color)
            ax.bar(i, player.diff[week], bottom = player.scores[week],
                    color = player.color, alpha = 0.4)

        plt.title('Week {}'.format(week+1))
        plt.xlabel('Week {}'.format(week+1))
        plt.xticks(index, n)
        plt.ylabel('Points')

        plt.savefig('graphs/Week {}.jpg'.format(week+1), dpi=300)
        plt.close()
