class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                max_good_integer = max(max_good_integer, num[i] * 3)
        return max_good_integer
