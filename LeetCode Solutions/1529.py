class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        current = '0'
        for char in target:
            if char != current:
                flips += 1
                current = char
        return flips
