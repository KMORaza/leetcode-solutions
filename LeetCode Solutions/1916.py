from collections import defaultdict
class Solution:
    def waysToBuildRooms(self, roomConnections):
        totalRooms = len(roomConnections)
        roomGraph = defaultdict(list)
        factorialValues = [1] * (totalRooms + 10)
        for index in range(2, len(factorialValues)):
            factorialValues[index] = factorialValues[index - 1] * index % 1000000007
        for roomIndex in range(1, totalRooms):
            parentRoomIndex = roomConnections[roomIndex]
            roomGraph[parentRoomIndex].append(roomIndex)
        finalResult = self._calculateWays(roomGraph, 0, factorialValues)
        return finalResult[1] % 1000000007
    def _calculateWays(self, roomGraph, currentRoomIndex, factorialValues):
        roomCount = [1, 0]
        totalSubRooms = 0
        subRoomResults = []
        for nextRoomIndex in roomGraph[currentRoomIndex]:
            subRoomOutcome = self._calculateWays(roomGraph, nextRoomIndex, factorialValues)
            totalSubRooms += subRoomOutcome[0]
            subRoomResults.append(subRoomOutcome)
        roomCount[0] += totalSubRooms
        combinationProduct = 1
        for sub in subRoomResults:
            chooseCombination = self._computeCombinations(totalSubRooms, sub[0], factorialValues)
            totalSubRooms -= sub[0]
            combinationProduct = combinationProduct * chooseCombination % 1000000007
            combinationProduct = combinationProduct * sub[1] % 1000000007
        roomCount[1] = combinationProduct
        return roomCount
    def _computeCombinations(self, total, select, factorialValues):
        if select > total:
            return 0
        totalFactorial = factorialValues[total]
        denominator = (factorialValues[total - select] * factorialValues[select]) % 1000000007
        inverseDenominator = pow(denominator, 1000000007 - 2, 1000000007)
        return (totalFactorial * inverseDenominator) % 1000000007
