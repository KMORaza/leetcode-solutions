class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        current_length = 0
        for char in s:
            if char == '1':
                current_length += 1
                count += current_length
            else:
                current_length = 0
        return count % (10**9 + 7)
