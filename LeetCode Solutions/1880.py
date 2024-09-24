class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def wordToNum(word):
            num = 0
            for char in word:
                num = num * 10 + (ord(char) - ord('a'))
            return num
        firstNum = wordToNum(firstWord)
        secondNum = wordToNum(secondWord)
        targetNum = wordToNum(targetWord)
        return firstNum + secondNum == targetNum
