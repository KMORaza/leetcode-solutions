class Solution:
    def digitCount(self, num: str) -> bool:
        count = [0] * 10
        for digit in num:
            count[int(digit)] += 1
        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False
        return True
