class Solution:
    def splitString(self, text: str) -> bool:
        return self.checkValidity(text, 0, -1, 0)
    def checkValidity(self, text: str, position: int, lastNum: int, segmentCount: int) -> bool:
        if position == len(text) and segmentCount > 1:
            return True
        currentNumber = 0
        for j in range(position, len(text)):
            currentNumber = currentNumber * 10 + int(text[j])
            if currentNumber > 9999999999:
                return False
            if (lastNum == -1 or currentNumber == lastNum - 1) and self.checkValidity(text, j + 1, currentNumber, segmentCount + 1):
                return True
        return False