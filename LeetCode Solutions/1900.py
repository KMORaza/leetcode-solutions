class Solution:
    def earliestAndLatest(self, totalPlayers: int, playerA: int, playerB: int) -> list[int]:
        minPlayer = min(playerA, playerB)
        maxPlayer = max(playerA, playerB)
        if minPlayer + maxPlayer == totalPlayers + 1:
            return [1, 1]
        if totalPlayers in (3, 4):
            return [2, 2]
        if minPlayer - 1 > totalPlayers - maxPlayer:
            minPlayer, maxPlayer = totalPlayers + 1 - maxPlayer, totalPlayers + 1 - minPlayer
        halfPlayers = (totalPlayers + 1) // 2
        minimumRounds = totalPlayers
        maximumRounds = 1
        if maxPlayer * 2 <= totalPlayers + 1:
            countA = minPlayer - 1
            countB = maxPlayer - minPlayer - 1
            for winsA in range(countA + 1):
                for winsB in range(countB + 1):
                    result = self.earliestAndLatest(halfPlayers, winsA + 1, winsA + winsB + 2)
                    minimumRounds = min(minimumRounds, 1 + result[0])
                    maximumRounds = max(maximumRounds, 1 + result[1])
        else:
            opposingPlayer = totalPlayers + 1 - maxPlayer
            countA = minPlayer - 1
            countB = opposingPlayer - minPlayer - 1
            intermediatePlayers = maxPlayer - opposingPlayer - 1
            for winsA in range(countA + 1):
                for winsB in range(countB + 1):
                    result = self.earliestAndLatest(halfPlayers, winsA + 1, winsA + winsB + 1 + (intermediatePlayers + 1) // 2 + 1)
                    minimumRounds = min(minimumRounds, 1 + result[0])
                    maximumRounds = max(maximumRounds, 1 + result[1])
        return [minimumRounds, maximumRounds]
