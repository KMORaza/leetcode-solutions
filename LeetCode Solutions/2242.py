import heapq
class Solution:
    def maximumScore(self, playerScores, connections):
        totalPlayers = len(playerScores)
        highestScore = -1
        graphAdjacency = [[] for _ in range(totalPlayers)]
        for nodeA, nodeB in connections:
            graphAdjacency[nodeA].append(nodeB)
            graphAdjacency[nodeB].append(nodeA)
            if len(graphAdjacency[nodeA]) > 3:
                graphAdjacency[nodeA] = heapq.nlargest(3, graphAdjacency[nodeA], key=lambda x: playerScores[x])
            if len(graphAdjacency[nodeB]) > 3:
                graphAdjacency[nodeB] = heapq.nlargest(3, graphAdjacency[nodeB], key=lambda x: playerScores[x])
        for nodeA, nodeB in connections:
            for childOne in graphAdjacency[nodeA]:
                for childTwo in graphAdjacency[nodeB]:
                    if childOne != childTwo and childOne != nodeB and childTwo != nodeA:
                        highestScore = max(highestScore, playerScores[childOne] + playerScores[nodeA] + playerScores[nodeB] + playerScores[childTwo])
        return highestScore