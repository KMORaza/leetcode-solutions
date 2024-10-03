class Solution:
    def maximumBobPoints(self, arrowCount, aliceScores):
        totalStates = (1 << 12) - 1
        highestAchievableScore = 0
        optimalState = 0
        for currentState in range(totalStates):
            canAchieve, currentScore = self.checkState(currentState, arrowCount, aliceScores)
            if canAchieve and currentScore > highestAchievableScore:
                highestAchievableScore = currentScore
                optimalState = currentState
        return self.distributeArrows(optimalState, arrowCount, aliceScores)
    def checkState(self, currentState, remainingArrows, aliceScores):
        score = 0
        for idx in range(12):
            if (currentState >> idx) & 1 == 1:
                remainingArrows -= aliceScores[idx] + 1
                score += idx
        return remainingArrows >= 0, score
    def distributeArrows(self, currentState, remainingArrows, aliceScores):
        bobArrowDistribution = [0] * 12
        for idx in range(12):
            if (currentState >> idx) & 1 == 1:
                bobArrowDistribution[idx] = aliceScores[idx] + 1
                remainingArrows -= aliceScores[idx] + 1
        bobArrowDistribution[0] = remainingArrows
        return bobArrowDistribution
