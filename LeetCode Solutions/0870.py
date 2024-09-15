from collections import Counter
from sortedcontainers import SortedDict
class Solution:
    def advantageCount(self, listA: list[int], listB: list[int]) -> list[int]:
        freqDict = SortedDict(Counter(listA))
        output = []
        for elementB in listB:
            pos = freqDict.bisect_right(elementB)
            if pos == len(freqDict):
                chosenKey = freqDict.peekitem(0)[0]
            else:
                chosenKey = freqDict.peekitem(pos)[0]
            output.append(chosenKey)
            if freqDict[chosenKey] == 1:
                del freqDict[chosenKey]
            else:
                freqDict[chosenKey] -= 1
        return output
