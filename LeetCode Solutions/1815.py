class Solution:
    def maxHappyGroups(self, groupSize: int, groupList: list[int]) -> int:
        happyCount = 0
        groupFrequency = [0] * groupSize
        for currentGroup in groupList:
            currentGroup %= groupSize
            if currentGroup == 0:
                happyCount += 1
            elif groupFrequency[groupSize - currentGroup] > 0:
                groupFrequency[groupSize - currentGroup] -= 1
                happyCount += 1
            else:
                groupFrequency[currentGroup] += 1
        return happyCount + self.calculate(tuple(groupFrequency), 0, groupSize)
    def __init__(self):
        self.cache = {}
    def calculate(self, groupFrequency: tuple[int], currentMod: int, groupSize: int) -> int:
        uniqueIdentifier = self.generateHash(groupFrequency)
        if uniqueIdentifier in self.cache:
            return self.cache[uniqueIdentifier]
        maximumHappy = 0
        if any(freq != 0 for freq in groupFrequency):
            for idx in range(len(groupFrequency)):
                if groupFrequency[idx] > 0:
                    newFrequency = list(groupFrequency)
                    newFrequency[idx] -= 1
                    maximumHappy = max(maximumHappy, self.calculate(tuple(newFrequency), (currentMod + idx) % groupSize, groupSize))
            if currentMod == 0:
                maximumHappy += 1
        self.cache[uniqueIdentifier] = maximumHappy
        return maximumHappy
    def generateHash(self, groupFrequency: tuple[int]) -> str:
        return "#" + "#".join(map(str, groupFrequency))
