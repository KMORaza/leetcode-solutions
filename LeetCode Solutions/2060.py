class Solution:
    def possiblyEquals(self, firstStr: str, secondStr: str) -> bool:
        firstLength = len(firstStr)
        secondLength = len(secondStr)
        dpMatrix = [[set() for _ in range(secondLength + 1)] for _ in range(firstLength + 1)]
        dpMatrix[0][0].add(0)
        for posFirst in range(firstLength + 1):
            for posSecond in range(secondLength + 1):
                for diff in dpMatrix[posFirst][posSecond]:
                    if diff <= 0:
                        tempNum = 0
                        for p in range(posFirst, min(posFirst + 3, firstLength)):
                            if firstStr[p].isdigit():
                                tempNum = tempNum * 10 + int(firstStr[p])
                                dpMatrix[p + 1][posSecond].add(diff + tempNum)
                            else:
                                break
                    if diff >= 0:
                        tempNum = 0
                        for q in range(posSecond, min(posSecond + 3, secondLength)):
                            if secondStr[q].isdigit():
                                tempNum = tempNum * 10 + int(secondStr[q])
                                dpMatrix[posFirst][q + 1].add(diff - tempNum)
                            else:
                                break
                    if posFirst < firstLength and diff < 0 and not firstStr[posFirst].isdigit():
                        dpMatrix[posFirst + 1][posSecond].add(diff + 1)
                    if posSecond < secondLength and diff > 0 and not secondStr[posSecond].isdigit():
                        dpMatrix[posFirst][posSecond + 1].add(diff - 1)
                    if posFirst < firstLength and posSecond < secondLength and diff == 0 and firstStr[posFirst] == secondStr[posSecond]:
                        dpMatrix[posFirst + 1][posSecond + 1].add(0)
        return 0 in dpMatrix[firstLength][secondLength]
