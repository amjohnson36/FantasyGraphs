class Player:
    def __init__(self, name, id, scores, maxs):
        self.name   = name
        self.id     = id
        self.scores = scores
        self.maxs   = maxs
        self.diff   = []
        self.avgscore = 0
        self.avgmax = 0
        self.byes = 0
        self.color = 'black'


    def printPlayer(self):
        print("Name: {}".format(self.name))
        print("ID: {}".format(self.id))
        print("Scores: {}".format(self.scores))
        print("Maxs: {}".format(self.maxs))
        print("Diffs: {}".format(self.diff))
        print("Average Score: {}".format(self.avgscore))
        print("Average Max: {}".format(self.avgmax))
        print("Ratio: {}\n".format(self.avgscore/self.avgmax))


    def checkByes(self):
        for score in range(len(self.scores)):
            if score == 0:
                self.byes += 1

    def setAverages(self):
        self.avgscore = sum(self.scores) / (len(self.scores) - self.byes)
        self.avgmax = sum(self.maxs) / (len(self.maxs) - self.byes)

    def setDiffs(self):
        for i in range(len(self.scores)):
            self.diff.append(self.maxs[i]-self.scores[i])

    def setColor(self, color):
        self.color = color
