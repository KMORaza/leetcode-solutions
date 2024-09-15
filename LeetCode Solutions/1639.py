class Solution:
    def numWays(self, words, target):
        x = 1000000007
        lenWord = len(words[0])
        lenTarget = len(target)
        dpTable = [[0] * (lenWord + 1) for _ in range(lenTarget + 1)]
        charCounts = [[0] * 26 for _ in range(lenWord)]
        for pos in range(lenWord):
            for word in words:
                charCounts[pos][ord(word[pos]) - ord('a')] += 1
        dpTable[0][0] = 1
        for tIdx in range(lenTarget + 1):
            for wIdx in range(lenWord):
                if tIdx < lenTarget:
                    dpTable[tIdx + 1][wIdx + 1] = (dpTable[tIdx][wIdx] * charCounts[wIdx][ord(target[tIdx]) - ord('a')]) % x
                dpTable[tIdx][wIdx + 1] = (dpTable[tIdx][wIdx + 1] + dpTable[tIdx][wIdx]) % x
        return dpTable[lenTarget][lenWord]
